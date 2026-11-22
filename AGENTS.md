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
| `images/headshot.jpg` | Square 800×800 crop of the headshot | Hero, beside the name |
| `images/team-ice-cream.jpg`, `images/team-dinner.jpg` | Team outing photos (1600×1200) | Research → Team |
| `images/class-undergrads.jpg` | Photo with undergraduate students (1600×900) | Teaching, beside the philosophy |
| `images/headshot-original.jpg` | Full-size original headshot | No |
| `images/teaching.jpg` | Teaching photo from the old site | No |
| `images/fig-*.jpg`, `images/fig-*.png` | Figures from the three "Selected work" papers (semantic similarity, EPPM, social signatures) | No (could illustrate Selected work) |

## Page structure (in `index.html`)
| Section | Element / id | Notes |
|---|---|---|
| Navigation | `<nav class="top">` | Links to the section ids below |
| Hero | `<header id="top">` | Network illustration (`<svg id="net">`, drawn by the script at the bottom), then the headshot (`img.headshot`) beside the name, title, intro and buttons |
| Research | `<section id="research">` | Three research areas, methods paragraph and tags, "Selected work" articles with `<details>` abstracts, "Team" photos (`<div class="team">` of `<figure class="photo">`) |
| Publications | `<section id="publications">` | `<ol class="pubs">` lists; each `<li>` is `<span class="yr">YEAR</span><span>citation</span>`; Yue's name in `<b>` |
| Teaching | `<section id="teaching">` | Philosophy with the class photo beside it, course tables (`class="stack"` makes them phone-friendly), student evaluation quotes |
| CV | `<section id="cv">` | Appointments and education timelines (`<ol class="tl">`), CV download button |
| Contact | `<footer id="contact">` | Contact links |

## Conventions
- Citations are in APA 7 style, newest first. Put Yue's name in `<b>` and journal names (with volume) in `<i>`. Link DOIs as `https://doi.org/...`.
- Use the colors defined as CSS variables at the top of the `<style>` block (`--sea`, `--sky`, `--pink`, and so on). Don't hard-code new colors.
- The page supports light and dark mode through `light-dark()` variables. Check both after changing styles.
- Check the layout at phone width (375px) as well as on desktop. Nothing should scroll sideways.
- Photos go in `images/` as JPEGs about 1600px on the long edge (roughly 200–400 KB), never full-size phone originals. Use `<figure class="photo">` with a short `<figcaption>`, and give each `<img>` width, height, alt text and `loading="lazy"`.
- Don't add frameworks, build tools or tracking scripts unless Yue asks for them.
- The network illustration script at the bottom of the file is self-contained. Leave it alone unless the task is about the illustration.

## Open to-do items (as of November 2026)
1. **Update content from the current CV.** The content was copied from the old Wix site and stops at September 2024. Add publications, presentations, grants and University of Kansas courses since then, and replace `files/Yue-Li-CV.pdf`.
2. **Add an email address** in the Contact section once Yue chooses one.
3. **Check two teaching-assistant entries.** COM 257 (Spring 2015) and COM 230 (Fall 2014) are listed under NC State. The old Wix site said Ohio State, but the dates and course numbers suggest NC State.
4. **Update the teaching statement.** It says "six years of college-level teaching," which is probably out of date.
5. **Optional:** use the research figures in `images/` to illustrate the "Selected work" articles.
