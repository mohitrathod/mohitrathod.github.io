from glob import glob
from os.path import dirname, realpath
import html
import re


currPath = dirname(realpath(__file__))
template = open(currPath + "/html/sitemap-template.html", "r", encoding="utf-8").read()

replacement = []

for indexFile in sorted(glob(currPath + "/blog/*.html")):
    with open(indexFile, "r", encoding="utf-8") as handle:
        content = handle.read()

    if 'class="java-toc"' not in content:
        continue

    heading = re.search(r"<h1[^>]*>(.*?)</h1>", content, re.S)
    if not heading:
        continue

    label = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", heading.group(1))).strip()
    indexUrl = "/blog/" + indexFile.rsplit("/", 1)[-1].replace(".html", "")
    replacement.append("")
    replacement.append("<a href='%s'>%s</a>" % (indexUrl, html.escape(label)))

    articles = re.findall(
        r'<a[^>]*class="java-article"[^>]*href="([^"]+)"[^>]*>.*?'
        r'<span class="java-article-title">(.*?)</span>',
        content,
        re.S,
    )
    for url, title in articles:
        title = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", title)).strip()
        replacement.append("  <a href='%s'>%s</a>" % (url, html.escape(title)))

sitemap = template.replace("_BLOCK_TO_REPLACE_", "\n".join(replacement))
with open(currPath + "/sitemap.html", "w", encoding="utf-8") as handle:
    handle.write(sitemap)

print("wrote sitemap.html with", sum(1 for line in replacement if line.strip().startswith("<a")), "links")
