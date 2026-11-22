# Instructions for coding agents (Codex, Claude, etc.)

This repository is the personal academic website of **Yue Li, Ph.D.**, served at **https://yueliphd.net** by GitHub Pages.

## How the site works
- It's a single static page: `index.html`. There's no build step, framework or package manager. HTML, CSS and JavaScript all live in that one file.
- GitHub Pages serves the `main` branch from the repository root. Every push to `main` goes live within a minute or two.
- `CNAME` holds the custom domain (`yueliphd.net`). Don't delete or rename it, or the domain stops working.
- `.nojekyll` tells GitHub Pages to serve files as they are. Keep it.
- Put PDFs (CV, syllabi, portfolio) in `files/` and images in `images/`, and link to them with relative paths such as `files/cv.pdf`.

## Page structure (in `index.html`)
| Section | Element / id | Notes |
|---|---|---|
| Navigation | `<nav class="top">` | Links to the section ids below |
| Hero | `<header id="top">` | Network illustration (`<svg id="net">`, drawn by the script at the bottom), portrait, name, title, intro, buttons |
| Research | `<section id="research">` | Three research areas, methods paragraph and tags, "Selected work" articles with `<details>` abstracts |
| Publications | `<section id="publications">` | `<ol class="pubs">` lists; each `<li>` is `<span class="yr">YEAR</span><span>citation</span>`; Yue's name in `<b>` |
| Teaching | `<section id="teaching">` | Philosophy, course tables (`class="stack"` makes them phone-friendly), student evaluation quotes |
| CV | `<section id="cv">` | Appointments and education timelines (`<ol class="tl">`), CV download button |
| Contact | `<footer id="contact">` | Contact links |

## Conventions
- Citations are in APA 7 style, newest first. Put Yue's name in `<b>` and journal names (with volume) in `<i>`. Link DOIs as `https://doi.org/...`.
- Use the colors defined as CSS variables at the top of the `<style>` block (`--sea`, `--sky`, `--pink`, and so on). Don't hard-code new colors.
- The page supports light and dark mode through `light-dark()` variables. Check both after changing styles.
- Check the layout at phone width (375px) as well as on desktop. Nothing should scroll sideways.
- Don't add frameworks, build tools or tracking scripts unless Yue asks for them.
- The network illustration script at the bottom of the file is self-contained. Leave it alone unless the task is about the illustration.

## Open to-do items (as of November 2026)
1. **Update content from the current CV.** The content was copied from the old Wix site and stops at September 2024. Add publications, presentations, grants and University of Kansas courses since then.
2. **Replace the portrait placeholder.** The hero shows a "YL" monogram inside `<div class="portrait">`. Add the photo as `images/headshot.jpg` (square, at least 600×600) and replace the letters with `<img src="images/headshot.jpg" alt="Yue Li">`.
3. **Move files off Wix.** The CV, syllabi and portfolio links point to `filesusr.com` (Wix). Download each one, add it to `files/` and update the links. Do this before the old Wix site is deleted, or the links break. The old addresses are listed in `WIX-FILES.md`.
4. **Add an email address** in the Contact section once Yue chooses one.
5. **Check two teaching-assistant entries.** COM 257 (Spring 2015) and COM 230 (Fall 2014) are listed under NC State. The old Wix site said Ohio State, but the dates and course numbers suggest NC State.
6. **Update the teaching statement.** It says "six years of college-level teaching," which is probably out of date.
