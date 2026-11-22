# COMS 930 tutorials: source

This folder is the source of the tutorial site at https://yueliphd.net/tutorials/coms930/.
The rendered site lives in `../coms930/`. Don't edit the files there by hand; they're rebuilt from this folder.

## Rebuild after a change
1. Install Quarto once: `pip install quarto-cli` (or download it from quarto.org).
2. From this folder, run `quarto render`.
3. Commit both this folder and `../coms930/`.

## What's here
- `_quarto.yml`: site settings, sidebar order, search, theme.
- `theme.scss`, `fonts.html`, `favicon.svg`: the look, matched to yueliphd.net.
- `index.qmd`: the overview page.
- `lab-*.md`: the R labs, converted from the knitted R Markdown output (code and output kept as text, so the labs aren't re-run).
- `*.ipynb`: the Colab notebooks as shown on the site, with a title block and Open in Colab / Download buttons added at the top.
- `downloads/`: the files students download or open in Colab (the original `.Rmd` labs and clean notebooks). `copy-downloads.py` copies them into `../coms930/` after each render.
- `output-class.lua`: used once to convert knitted labs; marks R output blocks.

## Adding a tutorial
- **Colab notebook:** put the clean notebook in `downloads/`. Put a copy here with a first raw cell holding YAML (`title`, `subtitle`, `description`) and a second markdown cell with the Open in Colab / Download buttons (copy one of the existing notebooks).
- **R lab:** put the `.Rmd` in `downloads/`, then add a `.qmd` or `.md` page here. A `.md` page shows code without running it. A `.qmd` page with `{r}` chunks would need R and the data to render.
- Add the page to the `render:` list and the sidebar in `_quarto.yml`, and to `index.qmd`. Add it to the COMS 930 list in the Teaching section of the site's main `index.html` too.
