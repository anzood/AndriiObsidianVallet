import re
import json

file_path = "pages/Links.md"

with open(file_path, "r") as f:
    lines = f.readlines()

content_start = 0
for i, line in enumerate(lines):
    if line.startswith("# Collections"):
        content_start = i + 1
        break

links_lines = lines[content_start:]
all_links = []
seen_urls = set()

# Regex to match [Title](URL) - Description #tags
structured_pattern = re.compile(r"^- \[(.*?)\]\((.*?)\) - (.*?) ((?:#\S+\s*)+)$")
title_url_pattern = re.compile(r"^- \[(.*?)\]\((.*?)\)(.*)$")
raw_url_pattern = re.compile(r"^-?\s*(https?://\S+)")

for line in links_lines:
    line = line.strip()
    if not line:
        continue

    url = None
    title = ""
    description = ""
    tags = []
    is_organized = False

    m = structured_pattern.match(line)
    if m:
        title, url, description, tags_str = m.groups()
        tags = [t.strip() for t in tags_str.split() if t.startswith("#")]
        is_organized = True
    else:
        m = title_url_pattern.match(line)
        if m:
            title, url, rest = m.groups()
            rest = rest.strip()
            if rest.startswith("- "):
                parts = rest.split(" #")
                description = parts[0].lstrip("- ").strip()
                if len(parts) > 1:
                    tags = ["#" + p.strip() for p in parts[1:]]
            if description and tags:
                is_organized = True
        else:
            m = raw_url_pattern.match(line)
            if m:
                url = m.group(1)
                is_organized = False

    if url:
        if url not in seen_urls:
            all_links.append(
                {
                    "title": title,
                    "url": url,
                    "description": description,
                    "tags": tags,
                    "is_organized": is_organized,
                }
            )
            seen_urls.add(url)

with open("all_links.json", "w") as f:
    json.dump(all_links, f)

unorganized = [al["url"] for al in all_links if not al["is_organized"]]
print(json.dumps(unorganized))
