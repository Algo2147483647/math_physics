from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path

from graph import Node, build_edge_in_graph, graph_to_json
from markdown import parse_kv_links, parse_section_in_markdown
from paths import DEFAULT_MARKDOWN_ROOT, DEFAULT_MATH_JSON_PATH


def build_graph_json_from_markdown_folder(
    folder_path: str | Path = DEFAULT_MARKDOWN_ROOT,
    output_path: str | Path = DEFAULT_MATH_JSON_PATH,
) -> dict[str, object]:
    graph = build_graph_from_markdown_folder(folder_path)
    graph_to_json(graph, output_path)
    return {
        "folder_path": str(Path(folder_path).resolve()),
        "output_path": str(Path(output_path).resolve()),
        "node_count": len(graph),
    }


def build_graph_from_markdown_folder(folder_path: str | Path) -> dict[str, Node]:
    folder = Path(folder_path).resolve()
    if not folder.exists():
        raise FileNotFoundError(f"Markdown folder not found: {folder}")

    graph: dict[str, Node] = {}
    for root, _, files in os.walk(folder):
        for file_name in sorted(files):
            file_path = Path(root) / file_name
            if file_path.suffix.lower() == ".md" and file_path.is_file():
                build_graph_from_markdown_file(file_path, graph)
    return graph


def build_graph_from_markdown_file(
    file_path: str | Path,
    graph: dict[str, Node],
) -> Node:
    markdown_path = Path(file_path).resolve()
    key = markdown_path.stem

    if key in graph:
        return graph[key]

    graph[key] = Node(key=key)

    try:
        content = markdown_path.read_text(encoding="utf-8")
    except OSError:
        return graph[key]

    define_section = parse_section_in_markdown(content, "Define")
    property_section = parse_section_in_markdown(content, "Properties")
    include_section = parse_section_in_markdown(content, "Include")
    parents_section = parse_section_in_markdown(content, "Parents")
    links = re.findall(r"\]\((.*?\.md)\)", include_section + "\n" + parents_section)

    graph[key].define = define_section
    graph[key].properties = [property_section]

    for link in links:
        linked_path = (markdown_path.parent / link).resolve()
        if linked_path.exists():
            build_graph_from_markdown_file(linked_path, graph)

    for child_key, label in parse_kv_links(include_section).items():
        if child_key in graph:
            build_edge_in_graph(graph, key, child_key, label)

    for parent_key, label in parse_kv_links(parents_section).items():
        if parent_key in graph:
            build_edge_in_graph(graph, parent_key, key, label)

    return graph[key]


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Build math/lib/math.json from Markdown notes."
    )
    parser.add_argument(
        "folder_path",
        nargs="?",
        default=str(DEFAULT_MARKDOWN_ROOT),
        help="Root folder that contains the Markdown concept notes.",
    )
    parser.add_argument(
        "--output",
        default=str(DEFAULT_MATH_JSON_PATH),
        help="Output path for the generated math.json file.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Print machine-readable JSON.",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    result = build_graph_json_from_markdown_folder(args.folder_path, args.output)
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"Markdown folder: {result['folder_path']}")
        print(f"Output JSON: {result['output_path']}")
        print(f"Node count: {result['node_count']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
