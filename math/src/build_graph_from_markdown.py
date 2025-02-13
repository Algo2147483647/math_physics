import os
import re
import json
from pathlib import Path
from graph import *
from markdown import *


def build_graph_json_from_markdown_folder(folder_path):
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
            define_section = parse_section_in_markdown(content, "Define")
            property_section = parse_section_in_markdown(content, "Properties")
            include_section = parse_section_in_markdown(content, "Include")
            parents_section = parse_section_in_markdown(content, "Parents")

            graph[name].define = define_section
            graph[name].properties.append(property_section)

            for link in links:
                link_path = os.path.abspath(os.path.join(os.path.dirname(file_path), link))
                build_graph_from_markdown_file(link_path, graph)

            for k, v in parse_kv_links(include_section).items():
                build_edge_in_graph(graph, name, k, v)

            for k, v in parse_kv_links(parents_section).items():
                build_edge_in_graph(graph, k, name, v)

            return graph[name]

    except IOError:
        return graph[name]









