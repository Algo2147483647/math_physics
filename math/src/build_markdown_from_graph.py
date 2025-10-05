from graph import *


def build_markdown_from_graph_json(json_file):
    graph = json_to_graph(json_file)
    build_markdown_from_graph(graph)
    return


def build_markdown_from_graph(graph):
    for key, node in graph.items():
        if key == "root":
            continue

        with open("D:/Algo/Notes/math_physics/math/" + node.key + ".md", 'w', encoding='utf-8') as file:
            file.write("# " + node.key.replace("_", " ") + "\n\n")
            file.write("[TOC]\n\n")
            file.write("## Define\n\n" + node.define + "\n\n")

            file.write("## Properties\n\n")
            for property in node.properties:
                file.write(property + "\n\n")

            file.write("## Include\n\n")
            for kid, value in node.kids.items():
                if kid == "root":
                    continue
                file.write("- [%s](./%s.md): %s\n\n" % (kid, kid, value))

            file.write("## Parents\n\n")
            for parent, value in node.parents.items():
                if parent == "root":
                    continue
                file.write("- [%s](./%s.md): %s\n\n" % (parent, parent, value))
    return


def add_kid_for_graph(json_file, key, kid_key):
    graph = json_to_graph(json_file)
    build_node_in_graph(graph, "kid", key, kid_key, "")
    graph_to_json(graph)
    build_markdown_from_graph(graph)
