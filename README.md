# Ali Reza Farshad Fard: resume site (GitHub Pages)

Live URL after publishing: https://ali-fard.github.io/alireza-farshadfard-cv/

## Publish (GitHub web UI)
1. github.com → New repository → name **alireza-farshadfard-cv** → Public → Create.
2. Add file → Upload files → drag in everything from this folder (including `assets/` and `.nojekyll`) → Commit.
3. Settings → Pages → Source: **Deploy from a branch** → Branch: `main` / `(root)` → Save. The site is live in 1–2 minutes.
4. Add the URL to LinkedIn (Contact info → Website) and to your GitHub profile.

## Edit
All text lives in `build.py` (profile, experience, skills, certificate, projects). Run `python3 build.py`, then upload the changed `.html` files.
The PDF in `assets/` is printed from `resume.html`; regenerate it after edits (Chrome → resume.html → Print → Save as PDF, margins default) and upload it with the same name.
