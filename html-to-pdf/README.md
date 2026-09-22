# Resume PDF generation (WSL/Linux)

Uses Python and Playwright's Chromium to convert the local `resume.html`
into `resume.pdf` at the repository root. Each run replaces that PDF.

## One-time setup

Run from the repository root:

```bash
python3 -m venv html-to-pdf/.venv
html-to-pdf/.venv/bin/python -m pip install -r html-to-pdf/requirements.txt
html-to-pdf/.venv/bin/python -m playwright install --with-deps chromium
```

If virtual-environment creation reports that `ensurepip` is missing, install
the matching venv package first (for example, `sudo apt install python3.14-venv`
for Python 3.14).

Installing browser system dependencies may require sudo. Internet access is
needed for installation and to load the resume's Google Fonts.

## Generate

```bash
./html-to-pdf/generate_resume.sh
```

The launcher resolves paths relative to itself, so it can also be invoked
by absolute path from any working directory. No virtual environment activation
is required. It uses the resume's print CSS and produces a tagged, text-based PDF.
