import os
import re
import json
from pathlib import Path
from graph import *


def build_graph_json_from_markdown_folder(folder_path):
    print(folder_path)
    result = build_graph_from_markdown_folder(folder_path)
    result = build_common_root(result)

    json_file = graph_to_json(result)
    return json_file


def build_graph_from_markdown_folder(folder_path):
    result = {}
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            if os.path.isfile(file_path) and file_name.endswith(".md"):
                build_graph_from_markdown_file(file_path, result)

    return result


def build_graph_from_markdown_file(file_path, graph):
    file_path = os.path.abspath(file_path)

    name = os.path.splitext(os.path.basename(file_path))[0]
    if name in graph:
        return graph[name]

    graph[name] = Node(
        name=name,
    )

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

            links = re.findall(r'\]\((.*?\.md)\)', content)
            define_section = re.search(r'##\s*Define(.*?)(\n## \w+|$)', content, re.DOTALL)
            define_section = define_section.group(1).strip() if define_section else ""
            property_section = re.search(r'##\s*Property(.*?)(\n## \w+|$)', content, re.DOTALL)
            property_section = property_section.group(1).strip() if property_section else ""

            graph[name].define = define_section
            graph[name].properties.append(property_section)

            for link in links:
                link_path = os.path.abspath(os.path.join(os.path.dirname(file_path), link))
                link_name = os.path.splitext(os.path.basename(link_path))[0]
                build_graph_from_markdown_file(link_path, graph)

                if define_section and link in graph[name].define:
                    build_edge(graph, link_name, name, "")
                else:
                    build_edge(graph, name, link_name, "")

            return graph[name]

    except IOError:
        return graph[name]
