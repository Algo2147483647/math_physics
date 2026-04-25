from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any

from _math_json_common import (
    DEFAULT_MATH_JSON_PATH,
    STANDARD_FIELDS,
    get_standard_field,
    load_concepts,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Validate math.json and emit a compact snapshot summary."
    )
    parser.add_argument(
        "--path",
        type=Path,
        default=DEFAULT_MATH_JSON_PATH,
        help="Path to math.json.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit machine-readable JSON.",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit non-zero on warnings as well as errors.",
    )
    return parser


def validate_node_shape(key: str, node: Any) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    if not isinstance(node, dict):
        errors.append(f"{key}: node is {type(node).__name__}, expected object")
        return errors, warnings

    missing = [field for field in STANDARD_FIELDS if field not in node]
    extra = [field for field in node if field not in STANDARD_FIELDS]
    if missing:
        errors.append(f"{key}: missing fields {missing}")
    if extra:
        warnings.append(f"{key}: extra fields {extra}")

    if "define" in node and not isinstance(node["define"], str):
        errors.append(f"{key}: define is {type(node['define']).__name__}, expected string")
    if "parents" in node and not isinstance(node["parents"], dict):
        errors.append(f"{key}: parents is {type(node['parents']).__name__}, expected object")
    if "children" in node and not isinstance(node["children"], dict):
        errors.append(f"{key}: children is {type(node['children']).__name__}, expected object")
    if "properties" in node:
        if not isinstance(node["properties"], list):
            errors.append(
                f"{key}: properties is {type(node['properties']).__name__}, expected array"
            )
        elif not all(isinstance(item, str) for item in node["properties"]):
            errors.append(f"{key}: properties contains non-string items")

    return errors, warnings


def format_edge_issue(
    source: str,
    field: str,
    target: str,
    label: str,
    reverse_field: str,
    reverse_label: str | None = None,
) -> str:
    base = f"{source}.{field} -> {target} ({label})"
    if reverse_label is None:
        return f"{base}; reverse {reverse_field}=<missing>"
    return f"{base}; reverse {reverse_field}={reverse_label}"


def main() -> int:
    args = build_parser().parse_args()
    concepts = load_concepts(args.path)

    errors: list[str] = []
    warnings: list[str] = []
    parent_labels: Counter[str] = Counter()
    child_labels: Counter[str] = Counter()
    property_lengths: Counter[int] = Counter()
    broken_references: list[str] = []
    mirrored_parent_edges = 0
    one_sided_parent_edges: list[str] = []
    mismatched_parent_edges: list[str] = []
    mirrored_child_edges = 0
    one_sided_child_edges: list[str] = []
    mismatched_child_edges: list[str] = []

    if not isinstance(concepts, dict):
        errors.append("Top-level JSON value is not an object.")
    else:
        for key, node in concepts.items():
            node_errors, node_warnings = validate_node_shape(key, node)
            errors.extend(node_errors)
            warnings.extend(node_warnings)

            if not isinstance(node, dict):
                continue

            parents = node.get("parents", {})
            children = node.get("children", {})
            properties = node.get("properties", [])

            if isinstance(parents, dict):
                parent_labels.update(parents.values())
                for target, label in parents.items():
                    if target not in concepts:
                        broken_references.append(f"{key}.parents -> {target} ({label})")
                        continue

                    reverse_label = get_standard_field(concepts[target], "children").get(key)
                    if reverse_label is None:
                        one_sided_parent_edges.append(
                            format_edge_issue(key, "parents", target, label, "children")
                        )
                    elif reverse_label == label:
                        mirrored_parent_edges += 1
                    else:
                        mismatched_parent_edges.append(
                            format_edge_issue(
                                key,
                                "parents",
                                target,
                                label,
                                "children",
                                reverse_label,
                            )
                        )
            if isinstance(children, dict):
                child_labels.update(children.values())
                for target, label in children.items():
                    if target not in concepts:
                        broken_references.append(f"{key}.children -> {target} ({label})")
                        continue

                    reverse_label = get_standard_field(concepts[target], "parents").get(key)
                    if reverse_label is None:
                        one_sided_child_edges.append(
                            format_edge_issue(key, "children", target, label, "parents")
                        )
                    elif reverse_label == label:
                        mirrored_child_edges += 1
                    else:
                        mismatched_child_edges.append(
                            format_edge_issue(
                                key,
                                "children",
                                target,
                                label,
                                "parents",
                                reverse_label,
                            )
                        )
            if isinstance(properties, list):
                property_lengths[len(properties)] += 1

    structural_issues = (
        one_sided_parent_edges
        + mismatched_parent_edges
        + one_sided_child_edges
        + mismatched_child_edges
    )

    payload = {
        "path": str(args.path),
        "concept_count": len(concepts) if isinstance(concepts, dict) else 0,
        "parent_edge_count": sum(parent_labels.values()),
        "child_edge_count": sum(child_labels.values()),
        "property_list_lengths": dict(sorted(property_lengths.items())),
        "parent_relation_labels": dict(parent_labels.most_common()),
        "child_relation_labels": dict(child_labels.most_common()),
        "mirrored_parent_edges": mirrored_parent_edges,
        "one_sided_parent_edges": one_sided_parent_edges,
        "mismatched_parent_edges": mismatched_parent_edges,
        "mirrored_child_edges": mirrored_child_edges,
        "one_sided_child_edges": one_sided_child_edges,
        "mismatched_child_edges": mismatched_child_edges,
        "broken_references": broken_references,
        "structural_issues": structural_issues,
        "errors": errors,
        "warnings": warnings,
    }

    if args.json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print(f"Path: {payload['path']}")
        print(f"Concept count: {payload['concept_count']}")
        print(f"Parent edges: {payload['parent_edge_count']}")
        print(f"Child edges: {payload['child_edge_count']}")
        print(f"Property list lengths: {payload['property_list_lengths']}")
        print(f"Mirrored parent edges: {payload['mirrored_parent_edges']}")
        print(f"One-sided parent edges: {len(payload['one_sided_parent_edges'])}")
        print(f"Mismatched parent edges: {len(payload['mismatched_parent_edges'])}")
        print(f"Mirrored child edges: {payload['mirrored_child_edges']}")
        print(f"One-sided child edges: {len(payload['one_sided_child_edges'])}")
        print(f"Mismatched child edges: {len(payload['mismatched_child_edges'])}")

        print("\nParent relation labels:")
        for label, count in payload["parent_relation_labels"].items():
            print(f"- {label}: {count}")

        print("\nChild relation labels:")
        for label, count in payload["child_relation_labels"].items():
            print(f"- {label}: {count}")

        print("\nBroken references:")
        if broken_references:
            for item in broken_references:
                print(f"- {item}")
        else:
            print("- <none>")

        print("\nOne-sided parent edges:")
        print("\n".join(f"- {item}" for item in payload["one_sided_parent_edges"]) or "- <none>")

        print("\nMismatched parent edges:")
        print("\n".join(f"- {item}" for item in payload["mismatched_parent_edges"]) or "- <none>")

        print("\nOne-sided child edges:")
        print("\n".join(f"- {item}" for item in payload["one_sided_child_edges"]) or "- <none>")

        print("\nMismatched child edges:")
        print("\n".join(f"- {item}" for item in payload["mismatched_child_edges"]) or "- <none>")

        print("\nErrors:")
        print("\n".join(f"- {item}" for item in errors) or "- <none>")
        print("\nWarnings:")
        print("\n".join(f"- {item}" for item in warnings) or "- <none>")

    if errors:
        return 1
    if args.strict and (warnings or broken_references or structural_issues):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
