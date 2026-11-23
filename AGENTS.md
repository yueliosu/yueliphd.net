# Instructions for coding agents (Codex, Claude, etc.)

This repository is the personal academic website of **Yue Li, Ph.D.**, served at **https://yueliphd.net** by GitHub Pages.

## How the site works
- It's a single static page: `index.html`. There's no build step, framework or package manager. HTML, CSS and JavaScript all live in that one file.
- GitHub Pages serves the `main` branch from the repository root. Every push to `main` goes live within a minute or two.
- `CNAME` holds the custom domain (`yueliphd.net`). Don't delete or rename it, or the domain stops working.
- `.nojekyll` tells GitHub Pages to serve files as they are. Keep it.
- PDFs live in `files/` and images in `images/`. Link to them with relative paths such as `files/Yue-Li-CV.pdf`.

## Files
| Path | What it is | Used on the page |
|---|---|---|
| `files/Yue-Li-CV.pdf` | CV, updated September 2024. Replace it with the current CV under the same name so the links keep working, and update the "CV last updated" note in the CV section. | Hero and CV buttons |
| `files/portfolio.pdf` | Advertising photography and graphic design portfolio from undergrad | CV section |
| `files/syllabus-COMM*.pdf` | Ohio State syllabi (COMM 2367, 3160, 3163, 3444, 3558, 3628) | Teaching table |
| `files/syllabus-COMS*.pdf` | University of Kansas syllabi: COMS 930 (Spring 2026), COMS 356 (Fall 2025), COMS 320 (Spring 2026). To post a newer one, upload it under the same name; the link just says "Syllabus" | Teaching table |
| `images/headshot.jpg` | Square 800×800 crop of the headshot | Hero, beside the name |
| `images/team-ice-cream.jpg`, `images/team-dinner.jpg` | Team outing photos (1600×1200) | Research → Team |
| `images/class-undergrads.jpg` | Photo with undergraduate students (1600×900) | Teaching, beside the philosophy |
| `images/headshot-original.jpg` | Full-size original headshot | No |
| `images/teaching.jpg` | Teaching photo from the old site | No |
| `tutorials/coms930/` | COMS 930 tutorial site built with Quarto (sidebar, search), plus the downloadable `.Rmd` and `.ipynb` files. Generated; don't edit by hand | Teaching → COMS 930 tutorials, and the COMS 930 row in the course table |
| `tutorials/coms930-src/` | Source of the tutorial site (`_quarto.yml`, pages, theme). Edit here, then run `quarto render`; see its `README.md` | No |
| `images/fig-*.jpg`, `images/fig-*.png` | Figures from three published papers (semantic similarity, EPPM, social signatures) | No (could illustrate the research lines) |

## Page structure (in `index.html`)
| Section | Element / id | Notes |
|---|---|---|
| Navigation | `<nav class="top">` | Links to the section ids below |
| Hero | `<header id="top">` | Network illustration (`<svg id="net">`, drawn by the script at the bottom), then the headshot (`img.headshot`) beside the name, title, intro and buttons |
| Research | `<section id="research">` | Methods statement (`<p class="approach">`) with method and software tags; four research lines (`<article class="line">`), each with an icon, number, title, short description, a "Published" list (`<ol class="pubs rl">`, some with `<details>` abstracts), and either an "ICA 2027 submissions—decisions pending" list (`<ol class="pubs rl pending">`, lines 1–3; citations exactly as Yue supplied them, no student markers) or a "Manuscripts under review" list (`<ul class="wip">`, line 4, with an optional `<span class="status">` badge); "Team" photos (`<div class="team">` of `<figure class="photo">`). ICA 2027 decisions are due 13 January 2027: then rename the heading and change "decision pending" in each citation (and add accepted papers to "Conference presentations" in Publications). When a paper is published, move it to "Published" and add it to the Publications section too |
| Publications | `<section id="publications">` | `<ol class="pubs">` lists; each `<li>` is `<span class="yr">YEAR</span><span>citation</span>`; Yue's name in `<b>`. Student collaborators are marked * (graduate) and † (undergraduate), explained in the `<p class="pubnote">` above the lists. Journal articles and conference presentations only; manuscripts under review are not listed |
| Grants | `<section id="grants">` | Funded internal grants only (Yue's choice), newest first, in the same `<ol class="pubs grants">` format with a wider year column. Don't list unfunded proposals |
| Teaching | `<section id="teaching">` | Philosophy with the class photo beside it, course tables (`class="stack"` makes them phone-friendly), student evaluation quotes |
| CV | `<section id="cv">` | Appointments and education timelines (`<ol class="tl">`), CV download button |
| Contact | `<footer id="contact">` | Contact links |

## Adding a tutorial
The COMS 930 tutorials are a small Quarto site. Edit the source in `tutorials/coms930-src/`, run `quarto render` there (install with `pip install quarto-cli`), and commit both `tutorials/coms930-src/` and the rebuilt `tutorials/coms930/`. Step-by-step instructions are in `tutorials/coms930-src/README.md`.
- Every tutorial page has Open in Colab / Download buttons at the top. "Open in Colab" links use `https://colab.research.google.com/github/yueliosu/yueliphd.net/blob/main/tutorials/coms930/NAME.ipynb`.
- Also list a new tutorial in the "COMS 930 tutorials" block of the Teaching section in `index.html`.
- Before publishing, remove API keys, personal file paths and student information, and credit any tutorial you adapted.

## Conventions
- Citations are in APA 7 style, newest first. Put Yue's name in `<b>` and journal names (with volume) in `<i>`. Link DOIs as `https://doi.org/...`.
- The color scheme is "rose-lilac": tinted strips (class `tint`, plus the nav and hero) use a lilac → rose → blue gradient, with deep plum-indigo text, purple buttons, blue links, and blue (accurate information) and pink (misinformation) in the network picture. Use the CSS variables at the top of the `<style>` block (`--ink`, `--muted`, `--purple`, `--blue`, `--pink`, `--g1`–`--g3` for the gradient, and so on). Don't hard-code new colors. The tutorial site's matching colors are in `tutorials/coms930-src/theme.scss` and `_quarto.yml`.
- The site always shows the light rose-lilac colors (`color-scheme: light`), whatever the visitor's device setting. Yue chose this. The second value in each `light-dark()` is an unused dark version, kept in case she wants a dark mode later.
- Check the layout at phone width (375px) as well as on desktop. Nothing should scroll sideways.
- Photos go in `images/` as JPEGs about 1600px on the long edge (roughly 200–400 KB), never full-size phone originals. Use `<figure class="photo">` with a short `<figcaption>`, and give each `<img>` width, height, alt text and `loading="lazy"`.
- Don't add frameworks, build tools or tracking scripts unless Yue asks for them.
- The network illustration script at the bottom of the file is self-contained. Leave it alone unless the task is about the illustration.

## Open to-do items (as of November 2026)
1. **Finish updating from the current CV.** Publications, conference presentations, courses and grants were updated from Yue's December 2026 working CV on November 22, 2026. The research section was reorganized into four research lines on November 24, 2026. Still to do once her CV is final: the appointments, and replacing `files/Yue-Li-CV.pdf`.
2. **Update the teaching statement.** It says "six years of college-level teaching," which is probably out of date.
3. **Optional:** use the research figures in `images/` to illustrate the research lines.
