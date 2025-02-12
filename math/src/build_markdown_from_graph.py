from graph import *


def build_markdown_from_graph_json(json_file):
    graph = json_to_graph(json_file)
    build_markdown_from_graph(graph)
    return


def build_markdown_from_graph(graph):
    for key, node in graph.items():
        if key == "root":
            continue

        with open("C:/Algo/Notes/math_physics/math/lib/" + node.name + ".md", 'w', encoding='utf-8') as file:
            file.write("# " + node.name.replace("_", " ") + "\n\n")
            file.write("[TOC]\n\n")
            file.write("## Define\n\n" + node.define + "\n\n")

            file.write("## Properties\n\n")
            for property in node.properties:
                file.write(property + "\n\n")

            file.write("## Include\n\n")
            for kid, value in node.kids.items():
                if key == "root":
                    continue
                file.write("- [%s](./%s.md): %s\n\n" % (kid, kid, value))

            file.write("## Parents\n\n")
            for parent, value in node.parents.items():
                if key == "root":
                    continue
                file.write("- [%s](./%s.md): %s\n\n" % (parent, parent, value))
    return


def add_kid_for_graph(json_file, name, kid_name):
    graph = json_to_graph(json_file)
    build_node_in_graph(graph, "kid", name, kid_name, "")
    graph_to_json(graph)
    build_markdown_from_graph(graph)
