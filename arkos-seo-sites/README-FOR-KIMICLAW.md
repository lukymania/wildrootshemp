# KIMI Claw Deployment Instructions

## What This Is
This package contains 5 complete static websites for the Arkos Bioscience SEO backlink network. Each site is a self-contained folder with an `index.html` file and an `assets/` folder containing logos and hero images.

## Your Mission
Deploy each website folder to its corresponding GitHub repository. The user has already created 5 repos. Follow the steps below for each site.

---

## Step-by-Step Deployment

### Step 1: Extract the ZIP
Extract this archive to access the site folders.

### Step 2: Deploy Each Site to Its Repo

For each site below, **upload ALL files from the source folder to the root of the matching repository**.

| # | Source Folder | Deploy To Repo | Domain It Will Serve |
|---|--------------|----------------|---------------------|
| 1 | `cbdreviewhouse-com/` | The repo for **cbdreviewhouse.com** | cbdreviewhouse.com |
| 2 | `cbdreviewhouse-info/` | The repo for **cbdreviewhouse.info** | cbdreviewhouse.info |
| 3 | `thecbdreviewers/` | The repo for **thecbdreviewers.com** | thecbdreviewers.com |
| 4 | `nanocbdlab/` | The repo for **nanocbdlab.com** | nanocbdlab.com |
| 5 | `nanocbdrankings/` | The repo for **nanocbdrankings.com** | nanocbdrankings.com |

### What to Upload Per Repo
Each repository should have these files at its root:

```
[repo-root]/
  index.html          <-- Main file (copy from the matching folder above)
  assets/
    logo.png          <-- Site logo
    hero.jpg          <-- Hero background image
```

### Example: Deploying cbdreviewhouse.com
1. Open the repo for `cbdreviewhouse.com`
2. Upload `cbdreviewhouse-com/index.html` to the repo root
3. Upload `cbdreviewhouse-com/assets/logo.png` to `assets/logo.png`
4. Upload `cbdreviewhouse-com/assets/hero.jpg` to `assets/hero.jpg`
5. Commit the files
6. Enable GitHub Pages in repo Settings > Pages (source: Deploy from a branch, branch: main, folder: / (root))
7. The site will be live at `https://[username].github.io/[repo-name]/` or a custom domain if configured

Repeat this exact process for all 5 repositories.

---

## File Checklist Per Site

Make sure each repo contains:
- [ ] `index.html` (the complete website, 60-100KB each)
- [ ] `assets/logo.png` (transparent PNG logo, 1-2MB each)
- [ ] `assets/hero.jpg` (hero background image, 100-800KB each)

The `shared-assets/` folder contains `arkos-product.png` which is an optional bonus image you can also upload to any repo's assets folder if desired (it is not referenced by the HTML but can be used for future content).

---

## Enable GitHub Pages for All 5 Repos

After uploading files to each repo, enable GitHub Pages:

1. Go to each repo on GitHub
2. Click **Settings** tab
3. Click **Pages** in the left sidebar
4. Under "Build and deployment", set:
   - Source: **Deploy from a branch**
   - Branch: **main** (or master) / **/ (root)**
5. Click **Save**
6. Wait 1-2 minutes for the site to deploy
7. The live URL will be shown (e.g., `https://[username].github.io/[repo-name]/`)

---

## Verify Deployment

After all 5 repos are deployed, verify each one loads correctly by visiting:

- [ ] https://[username].github.io/[cbdreviewhouse-repo]/
- [ ] https://[username].github.io/[cbdreviewhouse-info-repo]/
- [ ] https://[username].github.io/[thecbdreviewers-repo]/
- [ ] https://[username].github.io/[nanocbdlab-repo]/
- [ ] https://[username].github.io/[nanocbdrankings-repo]/

Each site should display its logo, navigation, hero section, and content about Arkos Bioscience.

---

## Summary of Sites

| Site | Arkos Rank | Style |
|------|-----------|-------|
| CBD Review House | #1 Editor's Choice | Professional review hub |
| CBD Review House Info | Featured in articles | Educational blog |
| The CBD Reviewers | #1 The GOAT | Fun, cartoon mascots, youth-focused |
| Nano CBD Lab | #1 Top Rated | Scientific, clinical, data-driven |
| Nano CBD Rankings | #1 Champion (9.8/10) | Championship leaderboard |

All 5 sites link to each other and to https://www.arkosbio.com with dofollow links.

---

## Questions?
If anything is unclear, ask the user for the exact GitHub repo URLs and this README can be updated with specific paths.
