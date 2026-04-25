from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from _math_json_common import (
    DEFAULT_MATH_JSON_PATH,
    load_concepts,
    render_relation_map,
    resolve_concept,
    select_fields,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Resolve a math.json concept key and print selected fields."
    )
    parser.add_argument("term", help="Concept key or natural-language term to resolve.")
    parser.add_argument(
        "--field",
        dest="fields",
        action="append",
        choices=["define", "parents", "children", "properties", "all"],
        help="Field to print. Repeat to request multiple fields. Default: all standard fields.",
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
        "--max-matches",
        type=int,
        default=5,
        help="Number of candidate matches to keep when fuzzy matching.",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    concepts = load_concepts(args.path)
    match, candidates = resolve_concept(
        args.term,
        concepts,
        max_matches=args.max_matches,
    )

    if not match:
        if args.json:
            print(
                json.dumps(
                    {
                        "query": args.term,
                        "resolved": None,
                        "candidates": [candidate.to_dict() for candidate in candidates],
                        "error": "No concept passed the fuzzy-match cutoff.",
                    },
                    ensure_ascii=False,
                    indent=2,
                )
            )
        else:
            print(f"Query: {args.term}")
            print("Resolved: <none>")
            print("Candidates:")
            for candidate in candidates:
                print(f"- {candidate.key} ({candidate.match_type}, {candidate.score:.3f})")
        return 2

    node = concepts[match.key]
    payload = {
        "query": args.term,
        "resolved": match.to_dict(),
        "candidates": [candidate.to_dict() for candidate in candidates],
        "fields": select_fields(node, args.fields),
    }

    if args.json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return 0

    print(f"Query: {args.term}")
    print(f"Resolved: {match.key} ({match.match_type}, {match.score:.3f})")
    if len(candidates) > 1:
        print("Alternatives:")
        for candidate in candidates[1:]:
            print(f"- {candidate.key} ({candidate.match_type}, {candidate.score:.3f})")

    fields = payload["fields"]
    if "define" in fields:
        print("\nDefinition:")
        print(fields["define"])
    if "parents" in fields:
        print("\nParents:")
        print("\n".join(render_relation_map(fields["parents"])))
    if "children" in fields:
        print("\nChildren:")
        print("\n".join(render_relation_map(fields["children"])))
    if "properties" in fields:
        print("\nProperties:")
        properties = fields["properties"]
        if not properties:
            print("- <empty>")
        else:
            for index, item in enumerate(properties, start=1):
                print(f"[{index}]")
                print(item if item else "<empty>")
    return 0


if __name__ == "__main__":
    sys.exit(main())
