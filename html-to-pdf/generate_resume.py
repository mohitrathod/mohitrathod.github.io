#!/usr/bin/env python3
"""Generate resume.pdf from the local resume.html using Chromium."""

from pathlib import Path

from playwright.sync_api import sync_playwright


def main():
    root = Path(__file__).resolve().parent.parent
    source = root / "resume.html"
    output = root / "resume.pdf"
    with sync_playwright() as p:
        browser = p.chromium.launch()
        try:
            page = browser.new_page()
            page.emulate_media(media="print")
            page.goto(source.as_uri(), wait_until="load")
            page.evaluate("document.fonts.ready")
            page.pdf(
                path=str(output),
                format="A4",
                print_background=True,
                prefer_css_page_size=True,
                tagged=True,
            )
        finally:
            browser.close()
    print(f"Generated {output}")


if __name__ == "__main__":
    main()
