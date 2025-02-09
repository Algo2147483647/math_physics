import json


class Node:
    def __init__(self, name= "", define= "", properties= "", kids=None, parents=None):
        self.name = name
        self.define = define
        self.properties = properties
        self.kids = kids if kids is not None else set()
        self.parents = parents if parents is not None else set()
        self.coordinate = (-1, -1)

    def to_dict(self):
        return {
            "name": self.name,
            "kids": list(self.kids),
            "parents": list(self.parents),
            "coordinate": list(self.coordinate)
        }


def graph_to_json(graph):
    return json.dumps({key: node.to_dict() for key, node in graph.items()})


def build_coordinates_of_dag(dag):
    build_common_root(dag)

    queue = [dag["root"]]
    level = -1

    while queue:
        n = len(queue)
        level += 1

        for index in range(n):
            node = queue.pop(0)
            node.coordinate = (level, index)

            for kid_name in node.kids:
                kid = dag[kid_name]
                if kid.coordinate is (-1, -1):
                    queue.append(kid)

    return dag


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