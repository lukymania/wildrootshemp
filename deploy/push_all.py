#!/usr/bin/env python3
"""Deploy all files (including sitemaps and robots.txt) to GitHub Pages."""
import urllib.request, json, base64, sys, os

PAT = sys.argv[1] if len(sys.argv) > 1 else ""
OWNER = "lukymania"

REPOS = {
    "cbdreviewhouse": "cbdreviewhouse",
    "cbdreviewhouse-info": "cbdreviewhouse-info",
    "thecbdreviewers": "thecbdreviewers",
    "nanocbdlab": "nanocbdlab",
    "nanocbdrankings": "nanocbdrankings",
}

def push_file(repo, path, local_path, pat):
    with open(local_path, "rb") as f:
        content = base64.b64encode(f.read()).decode()
    
    # Get existing file SHA (if any)
    url = f"https://api.github.com/repos/{OWNER}/{repo}/contents/{path}"
    req = urllib.request.Request(url, headers={"Authorization": f"token {pat}"})
    sha = None
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read())
            sha = data.get("sha")
    except:
        pass
    
    data = {"message": f"Add sitemap, robots.txt, and site updates ({path})", "content": content}
    if sha:
        data["sha"] = sha
    
    req = urllib.request.Request(url, data=json.dumps(data).encode(),
        headers={"Authorization": f"token {pat}", "Content-Type": "application/json"}, method="PUT")
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return True, f"HTTP {resp.status}"
    except urllib.error.HTTPError as e:
        return False, json.loads(e.read()).get("message", str(e.code))

FILES = ["index.html", "buyers-guide.html", "chart.html", "sitemap.xml", "robots.txt"]

success = 0
total = 0
for folder, repo in REPOS.items():
    print(f"\n=== {repo} ===")
    for fname in FILES:
        local = f"/mnt/agents/output/deploy/{folder}/{fname}"
        if not os.path.exists(local):
            print(f"  SKIP {fname} (not found)")
            continue
        total += 1
        print(f"  Pushing {fname}...", end=" ")
        ok, msg = push_file(repo, fname, local, PAT)
        if ok:
            print(f"OK")
            success += 1
        else:
            print(f"FAIL: {msg}")

print(f"\n{'='*50}")
print(f"DONE: {success}/{total} files deployed")
