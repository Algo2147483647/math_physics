from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from _math_json_common import (
    DEFAULT_MATH_JSON_PATH,
    get_standard_field,
    load_concepts,
    resolve_concept,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Compare two concepts in math.json."
    )
    parser.add_argument("left", help="First concept key or natural-language term.")
    parser.add_argument("right", help="Second concept key or natural-language term.")
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
    return parser


def direct_relations(
    left_key: str,
    left_node: dict,
    right_key: str,
    right_node: dict,
) -> list[dict[str, str]]:
    relations: list[dict[str, str]] = []
    for field, source_key, source_node, target_key in (
        ("parents", left_key, left_node, right_key),
        ("children", left_key, left_node, right_key),
        ("parents", right_key, right_node, left_key),
        ("children", right_key, right_node, left_key),
    ):
        label = get_standard_field(source_node, field).get(target_key)
        if label:
            relations.append(
                {
                    "source": source_key,
                    "field": field,
                    "target": target_key,
                    "label": label,
                }
            )
    return relations


def relation_overlap(
    left_map: dict[str, str],
    right_map: dict[str, str],
) -> list[dict[str, str]]:
    shared_keys = sorted(set(left_map) & set(right_map))
    return [
        {
            "concept": key,
            "left_label": left_map[key],
            "right_label": right_map[key],
        }
        for key in shared_keys
    ]


def main() -> int:
    args = build_parser().parse_args()
    concepts = load_concepts(args.path)

    left_match, left_candidates = resolve_concept(args.left, concepts)
    right_match, right_candidates = resolve_concept(args.right, concepts)

    if not left_match or not right_match:
        payload = {
            "left_query": args.left,
            "right_query": args.right,
            "left_resolved": left_match.to_dict() if left_match else None,
            "right_resolved": right_match.to_dict() if right_match else None,
            "left_candidates": [candidate.to_dict() for candidate in left_candidates],
            "right_candidates": [candidate.to_dict() for candidate in right_candidates],
            "error": "At least one concept could not be resolved confidently.",
        }
        if args.json:
            print(json.dumps(payload, ensure_ascii=False, indent=2))
        else:
            print(payload["error"])
        return 2

    left_key = left_match.key
    right_key = right_match.key
    left_node = concepts[left_key]
    right_node = concepts[right_key]

    payload = {
        "left": {
            "query": args.left,
            "resolved": left_match.to_dict(),
        },
        "right": {
            "query": args.right,
            "resolved": right_match.to_dict(),
        },
        "direct_relations": direct_relations(left_key, left_node, right_key, right_node),
        "shared_parents": relation_overlap(
            get_standard_field(left_node, "parents"),
            get_standard_field(right_node, "parents"),
        ),
        "shared_children": relation_overlap(
            get_standard_field(left_node, "children"),
            get_standard_field(right_node, "children"),
        ),
        "left_only_parents": sorted(
            set(get_standard_field(left_node, "parents"))
            - set(get_standard_field(right_node, "parents"))
        ),
        "right_only_parents": sorted(
            set(get_standard_field(right_node, "parents"))
            - set(get_standard_field(left_node, "parents"))
        ),
        "left_only_children": sorted(
            set(get_standard_field(left_node, "children"))
            - set(get_standard_field(right_node, "children"))
        ),
        "right_only_children": sorted(
            set(get_standard_field(right_node, "children"))
            - set(get_standard_field(left_node, "children"))
        ),
    }

    if args.json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return 0

    print(f"Left: {left_key} ({left_match.match_type}, {left_match.score:.3f})")
    print(f"Right: {right_key} ({right_match.match_type}, {right_match.score:.3f})")

    print("\nDirect relations:")
    if payload["direct_relations"]:
        for relation in payload["direct_relations"]:
            print(
                f"- {relation['source']} --{relation['field']}:{relation['label']}--> {relation['target']}"
            )
    else:
        print("- <none>")

    print("\nShared parents:")
    if payload["shared_parents"]:
        for item in payload["shared_parents"]:
            print(
                f"- {item['concept']} (left={item['left_label']}, right={item['right_label']})"
            )
    else:
        print("- <none>")

    print("\nShared children:")
    if payload["shared_children"]:
        for item in payload["shared_children"]:
            print(
                f"- {item['concept']} (left={item['left_label']}, right={item['right_label']})"
            )
    else:
        print("- <none>")

    print("\nLeft-only parents:")
    print("\n".join(f"- {item}" for item in payload["left_only_parents"]) or "- <none>")
    print("\nRight-only parents:")
    print("\n".join(f"- {item}" for item in payload["right_only_parents"]) or "- <none>")
    print("\nLeft-only children:")
    print("\n".join(f"- {item}" for item in payload["left_only_children"]) or "- <none>")
    print("\nRight-only children:")
    print("\n".join(f"- {item}" for item in payload["right_only_children"]) or "- <none>")
    return 0


if __name__ == "__main__":
    sys.exit(main())
