import json


class Node:
    def __init__(self, name= ""):
        self.name = name
        self.define = ""
        self.properties = []
        self.kids = {}
        self.parents = {}

    def to_dict(self):
        return {
            "name": self.name,
            "define": self.define,
            "properties": self.properties,
            "kids": self.kids,
            "parents": self.parents
        }


def build_edge(graph, a, b, weight):
    graph[a].kids[b] = weight
    graph[b].parents[a] = weight


def graph_to_json(graph):
    with open('../lib/math.json', 'w', encoding='utf-8') as file:
        json.dump({key: node.to_dict() for key, node in graph.items()}, file, sort_keys=True, indent=4)
    return json.dumps({key: node.to_dict() for key, node in graph.items()}, sort_keys=True)


def graph_to_json(json_file):
    try:
        with open(json_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
            graph = []
            for node_name, node_info in data.items():
                node = Node(name=node_name)
                node.define = node_info.get("define", "")
                node.properties = node_info.get("properties", [])
                node.kids = node_info.get("kids", {})
                node.parents = node_info.get("parents", {})
                graph.append(node)
            return graph
    except FileNotFoundError:
        print(f"文件 {json_file} 未找到。")
    except json.JSONDecodeError:
        print(f"无法解析 {json_file} 中的 JSON 数据。")
    return []


def build_common_root(dag):
    roots = get_all_roots(dag)
    dag["root"] = Node(
        name="root",
    )

    for root in roots:
        build_edge(dag, "root", root, "")

    return dag


def get_all_roots(dag):
    res = set(dag.keys())
    for value in dag.values():
        for kid in value.kids:
            res.discard(kid)
    return list(res)

