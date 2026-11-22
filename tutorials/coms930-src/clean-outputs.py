"""Prepare a notebook's saved outputs for the Quarto tutorial site.

Usage (from this folder):  python3 clean-outputs.py NAME.ipynb [MORE.ipynb ...]

Run it on the site copy of a notebook (not the one in downloads/) before
`quarto render`. It edits the notebook in place and is safe to run twice.

Why: when a notebook has HTML outputs (for example pandas tables), Quarto
adds require.js to the page, which clashes with the site's search and
sidebar scripts. This script:
  - turns each HTML output into a raw-HTML Markdown block, so require.js
    is not needed;
  - keeps only the <table> from Colab's interactive DataFrame outputs and
    drops their <script> code (it only works inside Colab);
  - removes interactive widget outputs (progress bars and the like), which
    can't run on a static page, keeping their plain-text version if any.
"""
import json
import re
import sys

TABLE = re.compile(r"<table\b.*?</table>", re.S | re.I)
SCRIPT = re.compile(r"<script\b.*?</script>", re.S | re.I)
WIDGET = "application/vnd.jupyter.widget-view+json"


def clean_html(html):
    if "<script" in html.lower():
        tables = TABLE.findall(html)
        html = "\n".join(tables) if tables else SCRIPT.sub("", html)
    return html.strip()


def clean_notebook(path):
    with open(path, encoding="utf-8") as f:
        nb = json.load(f)
    changed = 0
    for cell in nb.get("cells", []):
        outputs = []
        for out in cell.get("outputs", []):
            data = out.get("data")
            if data is not None:
                if WIDGET in data:
                    data.pop(WIDGET)
                    changed += 1
                    if not data:
                        continue
                if "text/html" in data:
                    html = data.pop("text/html")
                    html = "".join(html) if isinstance(html, list) else html
                    data["text/markdown"] = "```{=html}\n" + clean_html(html) + "\n```"
                    changed += 1
            outputs.append(out)
        if "outputs" in cell:
            cell["outputs"] = outputs
    nb.get("metadata", {}).pop("widgets", None)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)
        f.write("\n")
    print(f"{path}: {changed} output(s) cleaned")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    for p in sys.argv[1:]:
        clean_notebook(p)
