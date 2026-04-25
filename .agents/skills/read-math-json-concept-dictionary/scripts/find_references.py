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
        description="Inspect inbound references and mirror status for a concept."
    )
    parser.add_argument("term", help="Concept key or natural-language term.")
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


def collect_inbound(concepts: dict, target_key: str, field: str) -> list[dict[str, str]]:
    matches: list[dict[str, str]] = []
    for source_key, node in sorted(concepts.items()):
        label = get_standard_field(node, field).get(target_key)
        if label:
            matches.append({"source": source_key, "field": field, "label": label})
    return matches


def collect_mirror_status(concepts: dict, target_key: str) -> list[dict[str, str | bool]]:
    node = concepts[target_key]
    statuses: list[dict[str, str | bool]] = []

    for linked_key, label in sorted(get_standard_field(node, "parents").items()):
        reverse_label = get_standard_field(concepts.get(linked_key, {}), "children").get(target_key)
        statuses.append(
            {
                "source_field": "parents",
                "linked_concept": linked_key,
                "label": label,
                "reverse_field": "children",
                "reverse_label": reverse_label or "",
                "mirrored": reverse_label == label,
            }
        )

    for linked_key, label in sorted(get_standard_field(node, "children").items()):
        reverse_label = get_standard_field(concepts.get(linked_key, {}), "parents").get(target_key)
        statuses.append(
            {
                "source_field": "children",
                "linked_concept": linked_key,
                "label": label,
                "reverse_field": "parents",
                "reverse_label": reverse_label or "",
                "mirrored": reverse_label == label,
            }
        )

    return statuses


def main() -> int:
    args = build_parser().parse_args()
    concepts = load_concepts(args.path)
    match, candidates = resolve_concept(args.term, concepts)

    if not match:
        payload = {
            "query": args.term,
            "resolved": None,
            "candidates": [candidate.to_dict() for candidate in candidates],
            "error": "No concept passed the fuzzy-match cutoff.",
        }
        if args.json:
            print(json.dumps(payload, ensure_ascii=False, indent=2))
        else:
            print(payload["error"])
        return 2

    target_key = match.key
    payload = {
        "query": args.term,
        "resolved": match.to_dict(),
        "target_node": concepts[target_key],
        "inbound_parents": collect_inbound(concepts, target_key, "parents"),
        "inbound_children": collect_inbound(concepts, target_key, "children"),
        "mirror_status": collect_mirror_status(concepts, target_key),
    }

    if args.json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return 0

    print(f"Resolved: {target_key} ({match.match_type}, {match.score:.3f})")
    print("\nCurrent node:")
    print(json.dumps(payload["target_node"], ensure_ascii=False, indent=2))

    print("\nInbound parents references:")
    if payload["inbound_parents"]:
        for item in payload["inbound_parents"]:
            print(f"- {item['source']} -> {target_key} ({item['label']})")
    else:
        print("- <none>")

    print("\nInbound children references:")
    if payload["inbound_children"]:
        for item in payload["inbound_children"]:
            print(f"- {item['source']} -> {target_key} ({item['label']})")
    else:
        print("- <none>")

    print("\nMirror status for this node's own edges:")
    if payload["mirror_status"]:
        for item in payload["mirror_status"]:
            state = "mirrored" if item["mirrored"] else "one-sided"
            reverse = item["reverse_label"] or "<missing>"
            print(
                f"- {target_key}.{item['source_field']} -> {item['linked_concept']} ({item['label']}); "
                f"reverse {item['reverse_field']}={reverse} [{state}]"
            )
    else:
        print("- <none>")
    return 0


if __name__ == "__main__":
    sys.exit(main())
