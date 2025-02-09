import json


class Node:
    def __init__(self, name= "", define= "", properties= "", kids=None, parents=None):
        self.name = name
        self.define = define
        self.properties = properties
        self.kids = kids if kids is not None else set()
        self.parents = parents if parents is not None else set()

    def to_dict(self):
        return {
            "name": self.name,
            "kids": list(self.kids),
            "parents": list(self.parents),
            "define": self.define,
            "properties": self.properties,
        }


def graph_to_json(graph):
    return json.dumps({key: node.to_dict() for key, node in graph.items()})

def build_common_root(dag):
    roots = get_all_roots(dag)
    dag["root"] = Node(
        name="root",
    )

    for root in roots:
        dag["root"].kids.add(root)

    return dag


def get_all_roots(dag):
    res = set(dag.keys())
    for value in dag.values():
        for kid in value.kids:
            res.discard(kid)
    return list(res)