from glob import glob
from os.path import dirname, realpath
from xml.sax.saxutils import escape as xml_escape
import html
import re


currPath = dirname(realpath(__file__))
template = open(currPath + "/html/sitemap-template.html", "r", encoding="utf-8").read()

replacement = []
index_pages = []

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
        r'<span class="java-article-title">(.*?)</span>.*?'
        r'<time class="java-article-date" datetime="([^"]+)"',
        content,
        re.S,
    )
    article_pages = []
    for url, title, date in articles:
        title = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", title)).strip()
        replacement.append("  <a href='%s'>%s</a>" % (url, html.escape(title)))
        article_pages.append((url, date))

    index_pages.append(
        {
            "url": indexUrl + ".html",
            "lastmod": max(date for _, date in article_pages) if article_pages else "",
            "articles": article_pages,
        }
    )

sitemap = template.replace("_BLOCK_TO_REPLACE_", "\n".join(replacement))
with open(currPath + "/sitemap.html", "w", encoding="utf-8") as handle:
    handle.write(sitemap)

core_pages = [
    ("https://mohitrathod.com/", "2017-01-22"),
    ("https://mohitrathod.com/about", "2017-01-22"),
    ("https://mohitrathod.com/resume", "2017-01-22"),
    ("https://mohitrathod.com/blog.html", "2018-01-22"),
    ("https://mohitrathod.com/contact", ""),
    ("https://mohitrathod.com/sitemap", ""),
]

urls = list(core_pages)
for index in index_pages:
    urls.append(("https://mohitrathod.com" + index["url"], index["lastmod"]))
    for article_url, date in index["articles"]:
        urls.append(("https://mohitrathod.com" + article_url, date))

xml_lines = [
    '<?xml version="1.0" encoding="UTF-8"?>',
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
]
for loc, lastmod in urls:
    xml_lines.append("  <url>")
    xml_lines.append("    <loc>%s</loc>" % xml_escape(loc))
    if lastmod:
        xml_lines.append("    <lastmod>%s</lastmod>" % lastmod)
    xml_lines.append("  </url>")
xml_lines.append("</urlset>")

with open(currPath + "/sitemap.xml", "w", encoding="utf-8") as handle:
    handle.write("\n".join(xml_lines) + "\n")

print(
    "wrote sitemap.html with",
    sum(1 for line in replacement if line.strip().startswith("<a")),
    "links and sitemap.xml with",
    len(urls),
    "URLs",
)
