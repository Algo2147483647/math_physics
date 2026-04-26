from __future__ import annotations

import argparse
import json
import os
import sys
import tempfile
import time
from contextlib import contextmanager
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable, Literal


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
            "properties": list(self.properties),
            "children": dict(self.children),
            "parents": dict(self.parents),
        }

    def add_child(
        self,
        graph: Graph,
        child_key: str,
        label: str = "",
        *,
        create_missing: bool = True,
    ) -> Node | None:
        if not self.key:
            raise ValueError("Node.key is required before adding relationships.")

        child = ensure_node_in_graph(graph, child_key) if create_missing else graph.get(child_key)
        if child is None:
            return None

        self.children[child_key] = label
        child.parents[self.key] = label
        return child

    def add_parent(
        self,
        graph: Graph,
        parent_key: str,
        label: str = "",
        *,
        create_missing: bool = True,
    ) -> Node | None:
        if not self.key:
            raise ValueError("Node.key is required before adding relationships.")

        parent = ensure_node_in_graph(graph, parent_key) if create_missing else graph.get(parent_key)
        if parent is None:
            return None

        self.parents[parent_key] = label
        parent.children[self.key] = label
        return parent

    def remove_child(self, graph: Graph, child_key: str) -> bool:
        if child_key not in self.children:
            return False

        self.children.pop(child_key, None)
        child = graph.get(child_key)
        if child is not None:
            child.parents.pop(self.key, None)
        return True

    def remove_parent(self, graph: Graph, parent_key: str) -> bool:
        if parent_key not in self.parents:
            return False

        self.parents.pop(parent_key, None)
        parent = graph.get(parent_key)
        if parent is not None:
            parent.children.pop(self.key, None)
        return True


Graph = dict[str, Node]
GRAPH_LOCK_TIMEOUT_SECONDS = 10.0
GRAPH_LOCK_POLL_INTERVAL_SECONDS = 0.05


def ensure_node_in_graph(graph: Graph, key: str) -> Node:
    node = graph.get(key)
    if node is None:
        node = Node(key=key)
        graph[key] = node
    elif not node.key:
        node.key = key
    return node


def _graph_lock_path(json_path: Path) -> Path:
    return json_path.with_suffix(f"{json_path.suffix}.lock")


@contextmanager
def _acquire_graph_lock(json_path: Path):
    json_path.parent.mkdir(parents=True, exist_ok=True)
    lock_path = _graph_lock_path(json_path)
    deadline = time.monotonic() + GRAPH_LOCK_TIMEOUT_SECONDS
    lock_fd: int | None = None

    while True:
        try:
            lock_fd = os.open(lock_path, os.O_CREAT | os.O_EXCL | os.O_RDWR)
            os.write(lock_fd, str(os.getpid()).encode("ascii", errors="ignore"))
            break
        except FileExistsError:
            if time.monotonic() >= deadline:
                raise TimeoutError(f"Timed out waiting for graph lock: {lock_path}")
            time.sleep(GRAPH_LOCK_POLL_INTERVAL_SECONDS)

    try:
        yield
    finally:
        if lock_fd is not None:
            os.close(lock_fd)
        try:
            lock_path.unlink()
        except FileNotFoundError:
            pass


def _write_text_atomically(path: Path, text: str, *, encoding: str = "utf-8") -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp_path: Path | None = None

    try:
        with tempfile.NamedTemporaryFile(
            "w",
            encoding=encoding,
            dir=path.parent,
            delete=False,
            suffix=path.suffix,
        ) as handle:
            handle.write(text)
            temp_path = Path(handle.name)
        os.replace(temp_path, path)
    except Exception:
        if temp_path is not None:
            try:
                temp_path.unlink()
            except FileNotFoundError:
                pass
        raise


def _mutate_json_graph(
    path: str | Path,
    mutate: Callable[[Graph], object],
) -> tuple[Path, object]:
    json_path = Path(path)
    with _acquire_graph_lock(json_path):
        graph = json_to_graph(json_path)
        result = mutate(graph)
        graph_to_json(graph, json_path)
    return json_path, result


def sync_graph_relations(
    graph: Graph,
    *,
    prefer: Literal["children", "parents"] = "children",
    create_missing: bool = False,
) -> Graph:
    if prefer == "parents":
        for target, node in list(graph.items()):
            for source, label in list(node.parents.items()):
                parent = ensure_node_in_graph(graph, source) if create_missing else graph.get(source)
                if parent is None:
                    continue
                parent.children[target] = label

        for source, node in list(graph.items()):
            for target, label in list(node.children.items()):
                child = ensure_node_in_graph(graph, target) if create_missing else graph.get(target)
                if child is None:
                    continue
                child.parents[source] = label
        return graph

    for source, node in list(graph.items()):
        for target, label in list(node.children.items()):
            child = ensure_node_in_graph(graph, target) if create_missing else graph.get(target)
            if child is None:
                continue
            child.parents[source] = label

    for target, node in list(graph.items()):
        for source, label in list(node.parents.items()):
            parent = ensure_node_in_graph(graph, source) if create_missing else graph.get(source)
            if parent is None:
                continue
            parent.children[target] = label

    return graph


def build_edge_in_graph(graph: Graph, source: str, target: str, weight: str = "") -> None:
    ensure_node_in_graph(graph, source).add_child(graph, target, weight)


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


def replace_children(graph: Graph, key: str, children: dict[str, str]) -> Node:
    node = get_node_from_graph(graph, key)
    for child_key in list(node.children):
        node.remove_child(graph, child_key)
    for child_key, label in children.items():
        node.add_child(graph, child_key, label)
    return node


def replace_parents(graph: Graph, key: str, parents: dict[str, str]) -> Node:
    node = get_node_from_graph(graph, key)
    for parent_key in list(node.parents):
        node.remove_parent(graph, parent_key)
    for parent_key, label in parents.items():
        node.add_parent(graph, parent_key, label)
    return node


def get_node_from_graph(graph: Graph, key: str) -> Node:
    node = graph.get(key)
    if node is None:
        raise ValueError(f"Concept not found: {key}")
    return node


def list_nodes_in_graph(graph: Graph) -> list[str]:
    return sorted(graph)


def create_node_in_graph(
    graph: Graph,
    key: str,
    *,
    define: str = "",
    properties: list[str] | None = None,
    children: dict[str, str] | None = None,
    parents: dict[str, str] | None = None,
) -> Node:
    if key in graph:
        raise ValueError(f"Concept already exists: {key}")

    node = ensure_node_in_graph(graph, key)
    node.define = define
    node.properties = list(properties or [])

    for child_key, label in (children or {}).items():
        node.add_child(graph, child_key, label)
    for parent_key, label in (parents or {}).items():
        node.add_parent(graph, parent_key, label)
    return node


def update_node_in_graph(
    graph: Graph,
    key: str,
    *,
    define: str | None = None,
    properties: list[str] | None = None,
    children: dict[str, str] | None = None,
    parents: dict[str, str] | None = None,
    merge_relations: bool = False,
) -> Node:
    node = get_node_from_graph(graph, key)

    if define is not None:
        node.define = define
    if properties is not None:
        node.properties = list(properties)
    if children is not None:
        if merge_relations:
            for child_key, label in children.items():
                node.add_child(graph, child_key, label)
        else:
            replace_children(graph, key, children)
    if parents is not None:
        if merge_relations:
            for parent_key, label in parents.items():
                node.add_parent(graph, parent_key, label)
        else:
            replace_parents(graph, key, parents)
    return node


def delete_node_from_graph(graph: Graph, key: str) -> dict[str, int]:
    node = get_node_from_graph(graph, key)
    removed_parent_links = len(node.parents)
    removed_child_links = len(node.children)

    for parent_key in list(node.parents):
        node.remove_parent(graph, parent_key)
    for child_key in list(node.children):
        node.remove_child(graph, child_key)

    graph.pop(key, None)
    return {
        "removed_parent_links": removed_parent_links,
        "removed_child_links": removed_child_links,
    }


def add_child_in_graph(graph: Graph, key: str, child_key: str, label: str = "") -> Node:
    node = get_node_from_graph(graph, key)
    node.add_child(graph, child_key, label)
    return node


def add_parent_in_graph(graph: Graph, key: str, parent_key: str, label: str = "") -> Node:
    node = get_node_from_graph(graph, key)
    node.add_parent(graph, parent_key, label)
    return node


def remove_child_in_graph(graph: Graph, key: str, child_key: str) -> bool:
    node = get_node_from_graph(graph, key)
    return node.remove_child(graph, child_key)


def remove_parent_in_graph(graph: Graph, key: str, parent_key: str) -> bool:
    node = get_node_from_graph(graph, key)
    return node.remove_parent(graph, parent_key)


def serialize_graph(graph: Graph) -> dict[str, dict[str, object]]:
    sync_graph_relations(graph)
    return {key: node.to_dict() for key, node in sorted(graph.items())}


def graph_to_json(graph: Graph, json_file: str | Path) -> str:
    json_path = Path(json_file)
    payload = serialize_graph(graph)
    text = json.dumps(payload, ensure_ascii=False, sort_keys=True, indent=2)
    _write_text_atomically(json_path, text, encoding="utf-8")
    return text


def json_to_graph(json_file: str | Path) -> Graph:
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

    sync_graph_relations(graph)
    return graph


def list_nodes_in_json(path: str | Path) -> dict[str, object]:
    graph = json_to_graph(path)
    return {
        "path": str(Path(path).resolve()),
        "count": len(graph),
        "keys": list_nodes_in_graph(graph),
    }


def get_node_in_json(path: str | Path, key: str) -> dict[str, object]:
    graph = json_to_graph(path)
    node = get_node_from_graph(graph, key)
    return {
        "path": str(Path(path).resolve()),
        "key": key,
        "node": node.to_dict(),
    }


def create_node_in_json(
    path: str | Path,
    key: str,
    *,
    define: str = "",
    properties: list[str] | None = None,
    children: dict[str, str] | None = None,
    parents: dict[str, str] | None = None,
) -> dict[str, object]:
    json_path, node_payload = _mutate_json_graph(
        path,
        lambda graph: create_node_in_graph(
            graph,
            key,
            define=define,
            properties=properties,
            children=children,
            parents=parents,
        ).to_dict(),
    )
    return {
        "path": str(json_path.resolve()),
        "action": "create",
        "key": key,
        "node": node_payload,
    }


def update_node_in_json(
    path: str | Path,
    key: str,
    *,
    define: str | None = None,
    properties: list[str] | None = None,
    children: dict[str, str] | None = None,
    parents: dict[str, str] | None = None,
    merge_relations: bool = False,
) -> dict[str, object]:
    json_path, node_payload = _mutate_json_graph(
        path,
        lambda graph: update_node_in_graph(
            graph,
            key,
            define=define,
            properties=properties,
            children=children,
            parents=parents,
            merge_relations=merge_relations,
        ).to_dict(),
    )
    return {
        "path": str(json_path.resolve()),
        "action": "update",
        "key": key,
        "node": node_payload,
        "merge_relations": merge_relations,
    }


def delete_node_in_json(path: str | Path, key: str) -> dict[str, object]:
    json_path, summary = _mutate_json_graph(
        path,
        lambda graph: delete_node_from_graph(graph, key),
    )
    return {
        "path": str(json_path.resolve()),
        "action": "delete",
        "key": key,
        **summary,
    }


def add_child_in_json(
    path: str | Path,
    key: str,
    child_key: str,
    *,
    label: str = "",
) -> dict[str, object]:
    json_path, node_payload = _mutate_json_graph(
        path,
        lambda graph: add_child_in_graph(graph, key, child_key, label).to_dict(),
    )
    return {
        "path": str(json_path.resolve()),
        "action": "add_child",
        "key": key,
        "child_key": child_key,
        "label": label,
        "node": node_payload,
    }


def add_parent_in_json(
    path: str | Path,
    key: str,
    parent_key: str,
    *,
    label: str = "",
) -> dict[str, object]:
    json_path, node_payload = _mutate_json_graph(
        path,
        lambda graph: add_parent_in_graph(graph, key, parent_key, label).to_dict(),
    )
    return {
        "path": str(json_path.resolve()),
        "action": "add_parent",
        "key": key,
        "parent_key": parent_key,
        "label": label,
        "node": node_payload,
    }


def remove_child_in_json(path: str | Path, key: str, child_key: str) -> dict[str, object]:
    json_path, removed = _mutate_json_graph(
        path,
        lambda graph: remove_child_in_graph(graph, key, child_key),
    )
    return {
        "path": str(json_path.resolve()),
        "action": "remove_child",
        "key": key,
        "child_key": child_key,
        "removed": removed,
    }


def remove_parent_in_json(path: str | Path, key: str, parent_key: str) -> dict[str, object]:
    json_path, removed = _mutate_json_graph(
        path,
        lambda graph: remove_parent_in_graph(graph, key, parent_key),
    )
    return {
        "path": str(json_path.resolve()),
        "action": "remove_parent",
        "key": key,
        "parent_key": parent_key,
        "removed": removed,
    }


def _parse_relation_arg(value: str) -> tuple[str, str]:
    key, separator, label = value.partition("=")
    relation_key = key.strip()
    if not relation_key:
        raise ValueError(f"Invalid relation argument: {value!r}")
    return relation_key, label.strip() if separator else ""


def _relation_args_to_dict(values: list[str] | None) -> dict[str, str] | None:
    if values is None:
        return None

    relations: dict[str, str] = {}
    for value in values:
        key, label = _parse_relation_arg(value)
        relations[key] = label
    return relations


def _resolve_optional_properties(
    values: list[str] | None,
    *,
    clear: bool,
) -> list[str] | None:
    if clear and values:
        raise ValueError("Cannot combine --clear-properties with --property.")
    if clear:
        return []
    return values


def _resolve_optional_relations(
    values: list[str] | None,
    *,
    clear: bool,
    option_name: str,
) -> dict[str, str] | None:
    if clear and values:
        raise ValueError(f"Cannot combine {option_name} with relation values.")
    if clear:
        return {}
    return _relation_args_to_dict(values)


def _print_payload(payload: dict[str, object], *, as_json: bool) -> None:
    if as_json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return

    for key, value in payload.items():
        if isinstance(value, (dict, list)):
            print(f"{key}:")
            print(json.dumps(value, ensure_ascii=False, indent=2))
        else:
            print(f"{key}: {value}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Manage math.json concept graph directly.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    list_parser = subparsers.add_parser("list", help="List all concept keys in math.json.")
    list_parser.add_argument("path", help="Path to math.json.")
    list_parser.add_argument("--json", action="store_true", help="Print machine-readable JSON.")

    get_parser = subparsers.add_parser("get", help="Read a single concept node from math.json.")
    get_parser.add_argument("path", help="Path to math.json.")
    get_parser.add_argument("key", help="Concept key.")
    get_parser.add_argument("--json", action="store_true", help="Print machine-readable JSON.")

    create_parser = subparsers.add_parser("create", help="Create a new concept node.")
    create_parser.add_argument("path", help="Path to math.json.")
    create_parser.add_argument("key", help="New concept key.")
    create_parser.add_argument("--define", default="", help="Definition text.")
    create_parser.add_argument(
        "--property",
        dest="properties",
        action="append",
        help="Property block text. Repeat to add multiple entries.",
    )
    create_parser.add_argument(
        "--child",
        dest="children",
        action="append",
        help="Child relation as KEY or KEY=LABEL. Repeat to add multiple edges.",
    )
    create_parser.add_argument(
        "--parent",
        dest="parents",
        action="append",
        help="Parent relation as KEY or KEY=LABEL. Repeat to add multiple edges.",
    )
    create_parser.add_argument("--json", action="store_true", help="Print machine-readable JSON.")

    update_parser = subparsers.add_parser("update", help="Update an existing concept node.")
    update_parser.add_argument("path", help="Path to math.json.")
    update_parser.add_argument("key", help="Existing concept key.")
    update_parser.add_argument("--define", help="Replace the definition text.")
    update_parser.add_argument(
        "--property",
        dest="properties",
        action="append",
        help="Property block text. Repeat to replace with multiple entries.",
    )
    update_parser.add_argument(
        "--child",
        dest="children",
        action="append",
        help="Child relation as KEY or KEY=LABEL. Repeat to replace or merge edges.",
    )
    update_parser.add_argument(
        "--parent",
        dest="parents",
        action="append",
        help="Parent relation as KEY or KEY=LABEL. Repeat to replace or merge edges.",
    )
    update_parser.add_argument(
        "--clear-properties",
        action="store_true",
        help="Replace properties with an empty list.",
    )
    update_parser.add_argument(
        "--clear-children",
        action="store_true",
        help="Replace child relations with an empty mapping.",
    )
    update_parser.add_argument(
        "--clear-parents",
        action="store_true",
        help="Replace parent relations with an empty mapping.",
    )
    update_parser.add_argument(
        "--merge-relations",
        action="store_true",
        help="Merge provided child/parent relations instead of replacing them.",
    )
    update_parser.add_argument("--json", action="store_true", help="Print machine-readable JSON.")

    delete_parser = subparsers.add_parser("delete", help="Delete a concept node.")
    delete_parser.add_argument("path", help="Path to math.json.")
    delete_parser.add_argument("key", help="Concept key.")
    delete_parser.add_argument("--json", action="store_true", help="Print machine-readable JSON.")

    add_child_parser = subparsers.add_parser("add-child", help="Add one child relation.")
    add_child_parser.add_argument("path", help="Path to math.json.")
    add_child_parser.add_argument("key", help="Existing parent concept key.")
    add_child_parser.add_argument("child_key", help="Child concept key.")
    add_child_parser.add_argument("--label", default="", help="Relation label.")
    add_child_parser.add_argument("--json", action="store_true", help="Print machine-readable JSON.")

    add_parent_parser = subparsers.add_parser("add-parent", help="Add one parent relation.")
    add_parent_parser.add_argument("path", help="Path to math.json.")
    add_parent_parser.add_argument("key", help="Existing child concept key.")
    add_parent_parser.add_argument("parent_key", help="Parent concept key.")
    add_parent_parser.add_argument("--label", default="", help="Relation label.")
    add_parent_parser.add_argument("--json", action="store_true", help="Print machine-readable JSON.")

    remove_child_parser = subparsers.add_parser("remove-child", help="Remove one child relation.")
    remove_child_parser.add_argument("path", help="Path to math.json.")
    remove_child_parser.add_argument("key", help="Existing parent concept key.")
    remove_child_parser.add_argument("child_key", help="Child concept key.")
    remove_child_parser.add_argument("--json", action="store_true", help="Print machine-readable JSON.")

    remove_parent_parser = subparsers.add_parser("remove-parent", help="Remove one parent relation.")
    remove_parent_parser.add_argument("path", help="Path to math.json.")
    remove_parent_parser.add_argument("key", help="Existing child concept key.")
    remove_parent_parser.add_argument("parent_key", help="Parent concept key.")
    remove_parent_parser.add_argument("--json", action="store_true", help="Print machine-readable JSON.")

    return parser


def main() -> int:
    args = build_parser().parse_args()

    try:
        if args.command == "list":
            payload = list_nodes_in_json(args.path)
        elif args.command == "get":
            payload = get_node_in_json(args.path, args.key)
        elif args.command == "create":
            payload = create_node_in_json(
                args.path,
                args.key,
                define=args.define,
                properties=args.properties,
                children=_relation_args_to_dict(args.children),
                parents=_relation_args_to_dict(args.parents),
            )
        elif args.command == "update":
            if args.merge_relations and (args.clear_children or args.clear_parents):
                raise ValueError(
                    "Cannot combine --merge-relations with --clear-children or --clear-parents."
                )
            payload = update_node_in_json(
                args.path,
                args.key,
                define=args.define,
                properties=_resolve_optional_properties(
                    args.properties,
                    clear=args.clear_properties,
                ),
                children=_resolve_optional_relations(
                    args.children,
                    clear=args.clear_children,
                    option_name="--clear-children",
                ),
                parents=_resolve_optional_relations(
                    args.parents,
                    clear=args.clear_parents,
                    option_name="--clear-parents",
                ),
                merge_relations=args.merge_relations,
            )
        elif args.command == "delete":
            payload = delete_node_in_json(args.path, args.key)
        elif args.command == "add-child":
            payload = add_child_in_json(args.path, args.key, args.child_key, label=args.label)
        elif args.command == "add-parent":
            payload = add_parent_in_json(args.path, args.key, args.parent_key, label=args.label)
        elif args.command == "remove-child":
            payload = remove_child_in_json(args.path, args.key, args.child_key)
        else:
            payload = remove_parent_in_json(args.path, args.key, args.parent_key)
    except (FileNotFoundError, TimeoutError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        return 2

    _print_payload(payload, as_json=args.json)
    return 0


if __name__ == "__main__":
    sys.exit(main())
