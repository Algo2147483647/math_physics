from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path

from paths import DEFAULT_MATH_JSON_PATH


@dataclass
class Node:
    key: str = ""
    define: str = ""
    properties: list[str] = field(default_factory=list)
    children: dict[str, str] = field(default_factory=dict)
    parents: dict[str, str] = field(default_factory=dict)

    def to_dict(self) -> dict[str, object]:
        return {
            "define": self.define,
            "properties": self.properties,
            "children": self.children,
            "parents": self.parents,
        }


Graph = dict[str, Node]


def build_edge_in_graph(graph: Graph, source: str, target: str, weight: str = "") -> None:
    graph[source].children[target] = weight
    graph[target].parents[source] = weight


def build_node_in_graph(
    graph: Graph,
    relation_type: str,
    anchor_key: str,
    node_key: str,
    weight: str = "",
) -> Node | None:
    if node_key in graph:
        return graph[node_key]

    if anchor_key not in graph:
        return None

    graph[node_key] = Node(key=node_key)

    if relation_type == "kid":
        build_edge_in_graph(graph, anchor_key, node_key, weight)
    elif relation_type == "parent":
        build_edge_in_graph(graph, node_key, anchor_key, weight)

    return graph[node_key]


def serialize_graph(graph: Graph) -> dict[str, dict[str, object]]:
    return {key: node.to_dict() for key, node in sorted(graph.items())}


def graph_to_json(graph: Graph, json_file: str | Path = DEFAULT_MATH_JSON_PATH) -> str:
    json_path = Path(json_file)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    payload = serialize_graph(graph)
    text = json.dumps(payload, ensure_ascii=False, sort_keys=True, indent=2)
    json_path.write_text(text, encoding="utf-8")
    return text


def json_to_graph(json_file: str | Path = DEFAULT_MATH_JSON_PATH) -> Graph:
    json_path = Path(json_file)
    if not json_path.exists():
        raise FileNotFoundError(f"JSON file not found: {json_path}")

    try:
        data = json.loads(json_path.read_text(encoding="utf-8-sig"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"Failed to parse JSON file: {json_path}") from exc

    if not isinstance(data, dict):
        raise ValueError(f"Top-level JSON value must be an object: {json_path}")

    graph: Graph = {}
    for node_key, node_info in data.items():
        if not isinstance(node_info, dict):
            raise ValueError(f"Node '{node_key}' must be a JSON object.")

        graph[node_key] = Node(
            key=node_key,
            define=node_info.get("define", ""),
            properties=list(node_info.get("properties", [])),
            children=dict(node_info.get("children", {})),
            parents=dict(node_info.get("parents", {})),
        )
    return graph
