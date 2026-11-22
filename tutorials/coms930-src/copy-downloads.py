# Runs after `quarto render`: copies the downloadable originals (.Rmd and clean .ipynb)
# next to the rendered pages, so "Download" and "Open in Colab" links keep working.
import os, shutil, glob
out = os.environ.get("QUARTO_PROJECT_OUTPUT_DIR", "../coms930")
for f in glob.glob("downloads/*"):
    shutil.copy2(f, out)
