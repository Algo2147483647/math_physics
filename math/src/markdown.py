import re

def parse_section_in_markdown(content, name):
    section = re.search(r'##\s*' + re.escape(name) + r'(.*?)(\n## \w+|$)', content, re.DOTALL)
    section = section.group(1).strip() if section else ""
    return section


def parse_kv_links(content):
    lines = content.splitlines()
    result = {}
    for line in lines:
        match = re.match(r'- \[(.*?)\]\(.*?\):(.*?)$', line)
        if match:
            result[match.group(1)] = match.group(2).strip()
    return result