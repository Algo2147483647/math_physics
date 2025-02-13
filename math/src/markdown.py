import re

def parse_section_in_markdown(content, name):
    section = re.search(r'##\s*' + re.escape(name) + r'(.*?)(\n## \w+|$)', content, re.DOTALL)
    section = section.group(1).strip() if section else ""
    return section


def parse_kv_links(content):
    pattern = r'\]\((.*?)\.md\): (.*?)(?=\n- \[|$)'
    matches = re.findall(pattern, content, re.DOTALL)
    result = {match[0]: match[1].strip() for match in matches}
    return result