import json


class Node:
    def __init__(self, key=""):
        self.key = key
        self.define = ""
        self.properties = []
        self.kids = {}
        self.parents = {}

    def to_dict(self):
        return {
            "key": self.key,
            "define": self.define,
            "properties": self.properties,
            "kids": self.kids,
            "parents": self.parents
        }


def build_edge_in_graph(graph, a, b, weight=""):
    graph[a].kids[b] = weight
    graph[b].parents[a] = weight


def build_node_in_graph(graph, type, a, b, weight=""):
    if b in graph:
        return graph[b]

    if a not in graph:
        return None

    graph[b] = Node(b)

    if type == "kid":
        build_edge_in_graph(graph, a, b, weight)
    elif type == "parent":
        build_edge_in_graph(graph, b, a, weight)

    return graph[b]


def graph_to_json(graph):
    with open('../lib/math.json', 'w', encoding='utf-8') as file:
        json.dump({key: node.to_dict() for key, node in graph.items()}, file, sort_keys=True, indent=2)
    return json.dumps({key: node.to_dict() for key, node in graph.items()}, sort_keys=True)


def json_to_graph(json_file):
    try:
        with open(json_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
            graph = {}
            for node_key, node_info in data.items():
                node = Node(key=node_key)
                node.define = node_info.get("define", "")
                node.properties = node_info.get("properties", [])
                node.kids = node_info.get("kids", {})
                node.parents = node_info.get("parents", {})
                graph[node_key] = node
            return graph
    except FileNotFoundError:
        print(f"文件 {json_file} 未找到。")
    except json.JSONDecodeError:
        print(f"无法解析 {json_file} 中的 JSON 数据。")
    return []


def build_common_root(dag):
    roots = get_all_roots(dag)
    dag["root"] = Node(
        key="root",
    )

    for root in roots:
        if root == "root":
            continue
        build_edge_in_graph(dag, "root", root, "")

    return dag


def get_all_roots(dag):
    res = set(dag.keys())
    for value in dag.values():
        for kid in value.kids:
            res.discard(kid)
    return list(res)

