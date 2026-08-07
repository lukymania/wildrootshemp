# Push Instructions - Arkos SEO Fixes

## What Changed

### 1. thecbdreviewers.com - Skulls → Stars
All skull emojis (💀) replaced with star emojis (⭐). CSS classes renamed from `.skulls`/`.skull` to `.stars`/`.star`.

### 2. nanocbdrankings.com - Arkos Bioscience Added
The #1 rank in the leaderboard table was missing "Arkos Bioscience" as the brand name. Now shows "Arkos Bioscience" in the product name cell.

### 3. All 5 Sites - Sitemaps Created
`sitemap.xml` files for Google Search Console submission.

---

## Option A: Quick Push (Copy-Paste Commands)

Run these commands one at a time in your terminal. Replace `YOUR_PAT` with your GitHub token.

### Step 1: Clone the repos
```bash
cd /tmp
export PAT="YOUR_PAT"

# Clone all 5 repos (shallow clone for speed)
git clone --depth 1 https://$PAT@github.com/lukymania/thecbdreviewers.git
git clone --depth 1 https://$PAT@github.com/lukymania/nanocbdrankings.git
git clone --depth 1 https://$PAT@github.com/lukymania/cbdreviewhouse.git
git clone --depth 1 https://$PAT@github.com/lukymania/cbdreviewhouse-info.git
git clone --depth 1 https://$PAT@github.com/lukymania/nanocbdlab.git
```

### Step 2: Apply the fixes
```bash
# 1. Fix thecbdreviewers - replace index.html with fixed version
curl -sL "https://raw.githubusercontent.com/lukymania/arkos-seo-fixes/main/thecbdreviewers-index.html" > thecbdreviewers/index.html

# 2. Fix nanocbdrankings - replace index.html with fixed version  
curl -sL "https://raw.githubusercontent.com/lukymania/arkos-seo-fixes/main/nanocbdrankings-index.html" > nanocbdrankings/index.html

# 3. Add sitemaps to all 5 repos
for repo in cbdreviewhouse cbdreviewhouse-info thecbdreviewers nanocbdlab nanocbdrankings; do
  domain=${repo//-/.}
  [ "$repo" == "cbdreviewhouse" ] && domain="cbdreviewhouse.com"
  [ "$repo" == "cbdreviewhouse-info" ] && domain="cbdreviewhouse.info"
  [ "$repo" == "thecbdreviewers" ] && domain="thecbdreviewers.com"
  [ "$repo" == "nanocbdlab" ] && domain="nanocbdlab.com"
  [ "$repo" == "nanocbdrankings" ] && domain="nanocbdrankings.com"
  
  cat > "$repo/sitemap.xml" << EOF
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://$domain/</loc>
    <lastmod>2025-05-13</lastmod>
    <priority>0.9</priority>
    <changefreq>weekly</changefreq>
  </url>
</urlset>
EOF
  echo "Created sitemap.xml for $domain"
done
```

### Step 3: Commit and push all changes
```bash
for repo in thecbdreviewers nanocbdrankings; do
  cd "$repo"
  git add index.html
  git commit -m "Fix: skulls to stars, Arkos brand name, SEO improvements"
  git push
  cd ..
done

for repo in cbdreviewhouse cbdreviewhouse-info thecbdreviewers nanocbdlab nanocbdrankings; do
  cd "$repo"
  git add sitemap.xml
  git commit -m "Add sitemap.xml for Google Search Console"
  git push
  cd ..
done
```

---

## Option B: Download and Manually Upload

1. Download the 7 files from this folder
2. For each file, upload to the matching repo on GitHub:
   - `thecbdreviewers-index.html` → Upload to `thecbdreviewers` repo as `index.html`
   - `nanocbdrankings-index.html` → Upload to `nanocbdrankings` repo as `index.html`
   - `*-sitemap.xml` → Upload to matching repo as `sitemap.xml`

---

## After Pushing: Submit to Google

Once deployed, submit each sitemap to Google Search Console:

| Site | Sitemap URL to Submit |
|------|----------------------|
| cbdreviewhouse.com | `https://cbdreviewhouse.com/sitemap.xml` |
| cbdreviewhouse.info | `https://cbdreviewhouse.info/sitemap.xml` |
| thecbdreviewers.com | `https://thecbdreviewers.com/sitemap.xml` |
| nanocbdlab.com | `https://nanocbdlab.com/sitemap.xml` |
| nanocbdrankings.com | `https://nanocbdrankings.com/sitemap.xml` |

Go to https://search.google.com/search-console → Select property → Sitemaps → Enter URL → Submit
