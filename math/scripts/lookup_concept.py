from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from _math_json_common import (
    load_concepts,
    render_relation_map,
    resolve_concept,
    select_fields,
)


def lookup_concept(
    term: str,
    *,
    fields: list[str] | None = None,
    path: str | Path,
    max_matches: int = 5,
) -> dict[str, object]:
    concepts = load_concepts(path)
    match, candidates = resolve_concept(term, concepts, max_matches=max_matches)
    payload = {
        "query": term,
        "resolved": match.to_dict() if match else None,
        "candidates": [candidate.to_dict() for candidate in candidates],
    }

    if not match:
        payload["error"] = "No concept passed the fuzzy-match cutoff."
        return payload

    payload["fields"] = select_fields(concepts[match.key], fields)
    return payload


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
        required=True,
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
    payload = lookup_concept(
        args.term,
        fields=args.fields,
        path=args.path,
        max_matches=args.max_matches,
    )

    if args.json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return 0 if payload.get("resolved") else 2

    print(f"Query: {payload['query']}")
    if not payload.get("resolved"):
        print("Resolved: <none>")
        print("Candidates:")
        for candidate in payload["candidates"]:
            print(f"- {candidate['key']} ({candidate['match_type']}, {candidate['score']:.3f})")
        return 2

    resolved = payload["resolved"]
    print(f"Resolved: {resolved['key']} ({resolved['match_type']}, {resolved['score']:.3f})")
    if len(payload["candidates"]) > 1:
        print("Alternatives:")
        for candidate in payload["candidates"][1:]:
            print(f"- {candidate['key']} ({candidate['match_type']}, {candidate['score']:.3f})")

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
