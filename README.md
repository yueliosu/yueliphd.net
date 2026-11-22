# yueliphd.net

Personal academic website of Yue Li, Ph.D. The live site is at **https://yueliphd.net**.

## Editing the site
- **With Codex or another coding agent:** open this repository and describe the change, for example "Add my 2025 article in *Health Communication* to the publications list." The agent reads `AGENTS.md` for the site's structure and conventions.
- **By hand on github.com:** open `index.html`, click the pencil icon, make the change and click **Commit changes**.

Changes go live within a minute or two of being saved to the `main` branch.

## How it's hosted
- **Hosting:** GitHub Pages, free, served from the `main` branch.
- **Domain:** `yueliphd.net` is registered with Wix and paid through **July 26, 2027**. Its DNS records point to GitHub Pages. The domain can be moved to another registrar (such as Cloudflare or Porkbun) any time before then. Turn off the registrar lock in Wix, get the transfer code, and start the transfer at the new registrar. The DNS records below need to be recreated there.

DNS records:

| Type | Host | Value |
|---|---|---|
| A | @ | 185.199.108.153 |
| A | @ | 185.199.109.153 |
| A | @ | 185.199.110.153 |
| A | @ | 185.199.111.153 |
| CNAME | www | *github-username*.github.io |

## To do
See the list at the end of `AGENTS.md`. The files that still need to be moved off Wix are listed in `WIX-FILES.md`.
