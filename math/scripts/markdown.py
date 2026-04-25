import re


def parse_section_in_markdown(content, name):
    pattern = r"##\s*" + re.escape(name) + r"(.*?)(\n##\s+.+|$)"
    section = re.search(pattern, content, re.DOTALL)
    return section.group(1).strip() if section else ""


def parse_kv_links(content):
    lines = content.splitlines()
    result = {}
    for line in lines:
        match = re.match(r"-\s+\[(.*?)\]\(.*?\)\s*:\s*(.*?)$", line.strip())
        if match:
            result[match.group(1)] = match.group(2).strip()
    return result
