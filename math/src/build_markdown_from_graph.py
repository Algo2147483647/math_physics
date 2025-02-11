from graph import *


def build_markdown_from_graph(json_file):
    graph = graph_to_json(json_file)

    for node in graph:
        with open("C:/Algo/Notes/math_physics/math/lib/" + node.name + ".md", 'w', encoding='utf-8') as file:
            file.write("# " + node.name.replace("_", " ") + "\n\n")
            file.write("[TOC]\n\n")
            file.write("## Define\n\n" + node.define + "\n\n")

            file.write("## Properties\n\n")
            for property in node.properties:
                file.write(property + "\n\n")

            file.write("## Include\n\n")
            for kid, value in node.kids.items():
                file.write("- [%s](./%s.md): %s\n\n" % (kid, kid, value))

            file.write("## Parents\n\n")
            for parent, value in node.parents.items():
                file.write("- [%s](./%s.md): %s\n\n" % (parent, parent, value))
    return


