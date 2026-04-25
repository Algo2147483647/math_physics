from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from graph import build_node_in_graph, graph_to_json, json_to_graph
from paths import DEFAULT_MARKDOWN_ROOT, DEFAULT_MATH_JSON_PATH


def build_markdown_from_graph_json(
    json_file: str | Path = DEFAULT_MATH_JSON_PATH,
    output_dir: str | Path = DEFAULT_MARKDOWN_ROOT,
) -> dict[str, object]:
    graph = json_to_graph(json_file)
    return build_markdown_from_graph(graph, output_dir)


def build_markdown_from_graph(
    graph,
    output_dir: str | Path = DEFAULT_MARKDOWN_ROOT,
) -> dict[str, object]:
    target_dir = Path(output_dir).resolve()
    target_dir.mkdir(parents=True, exist_ok=True)

    written_files = 0
    for key, node in sorted(graph.items()):
        if key == "root":
            continue

        markdown_path = target_dir / f"{key}.md"
        lines = [
            f"# {key.replace('_', ' ')}",
            "",
            "[TOC]",
            "",
            "## Define",
            "",
            node.define,
            "",
            "## Properties",
            "",
        ]

        properties = node.properties or [""]
        for item in properties:
            lines.extend([item, ""])

        lines.extend(["## Include", ""])
        for child, label in sorted(node.children.items()):
            if child == "root":
                continue
            lines.extend([f"- [{child}](./{child}.md): {label}", ""])

        lines.extend(["## Parents", ""])
        for parent, label in sorted(node.parents.items()):
            if parent == "root":
                continue
            lines.extend([f"- [{parent}](./{parent}.md): {label}", ""])

        markdown_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
        written_files += 1

    return {
        "output_dir": str(target_dir),
        "node_count": len(graph),
        "written_files": written_files,
    }


def add_kid_for_graph(
    json_file: str | Path,
    key: str,
    kid_key: str,
    weight: str = "",
    output_dir: str | Path = DEFAULT_MARKDOWN_ROOT,
) -> dict[str, object]:
    graph = json_to_graph(json_file)
    if key not in graph:
        raise ValueError(f"Parent concept not found: {key}")

    build_node_in_graph(graph, "kid", key, kid_key, weight)
    graph_to_json(graph, json_file)
    build_result = build_markdown_from_graph(graph, output_dir)
    build_result.update(
        {
            "json_file": str(Path(json_file).resolve()),
            "parent": key,
            "child": kid_key,
            "weight": weight,
        }
    )
    return build_result


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Generate Markdown notes from math.json or update graph nodes."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    build_parser = subparsers.add_parser("build", help="Write Markdown notes from math.json.")
    build_parser.add_argument(
        "json_file",
        nargs="?",
        default=str(DEFAULT_MATH_JSON_PATH),
        help="Path to math.json.",
    )
    build_parser.add_argument(
        "--output-dir",
        default=str(DEFAULT_MARKDOWN_ROOT),
        help="Directory where Markdown files will be written.",
    )
    build_parser.add_argument("--json", action="store_true", help="Print machine-readable JSON.")

    add_kid_parser = subparsers.add_parser("add-kid", help="Add a child node and rebuild outputs.")
    add_kid_parser.add_argument("json_file", help="Path to math.json.")
    add_kid_parser.add_argument("key", help="Existing parent concept key.")
    add_kid_parser.add_argument("kid_key", help="New child concept key.")
    add_kid_parser.add_argument(
        "--weight",
        default="",
        help="Relation label to store on the new edge.",
    )
    add_kid_parser.add_argument(
        "--output-dir",
        default=str(DEFAULT_MARKDOWN_ROOT),
        help="Directory where Markdown files will be written.",
    )
    add_kid_parser.add_argument("--json", action="store_true", help="Print machine-readable JSON.")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    if args.command == "add-kid":
        result = add_kid_for_graph(
            args.json_file,
            args.key,
            args.kid_key,
            weight=args.weight,
            output_dir=args.output_dir,
        )
        as_json = args.json
    else:
        result = build_markdown_from_graph_json(args.json_file, args.output_dir)
        as_json = args.json

    if as_json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        for key, value in result.items():
            print(f"{key}: {value}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
