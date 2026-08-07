#!/usr/bin/env python3
"""
Deploy all 5 SEO site files to GitHub Pages.
Usage: python push_to_github.py YOUR_GITHUB_PAT
"""
import urllib.request, json, base64, sys, os

if len(sys.argv) < 2:
    print("Usage: python push_to_github.py YOUR_GITHUB_PAT")
    print("Get a PAT at: https://github.com/settings/tokens")
    sys.exit(1)

PAT = sys.argv[1]
OWNER = "lukymania"

# Repo mapping: folder_name -> repo_name
REPOS = {
    "cbdreviewhouse": "cbdreviewhouse",
    "cbdreviewhouse-info": "cbdreviewhouse-info",
    "thecbdreviewers": "thecbdreviewers",
    "nanocbdlab": "nanocbdlab",
    "nanocbdrankings": "nanocbdrankings",
}

# Files to push for each repo
FILES_TO_PUSH = ["index.html", "buyers-guide.html", "chart.html"]

def github_api(method, endpoint, data=None, pat=PAT):
    url = f"https://api.github.com{endpoint}"
    headers = {
        "Authorization": f"token {pat}",
        "Accept": "application/vnd.github.v3+json"
    }
    if data:
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(
        url,
        data=json.dumps(data).encode() if data else None,
        headers=headers,
        method=method
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return json.loads(resp.read()), resp.status
    except urllib.error.HTTPError as e:
        err_body = e.read().decode()
        try:
            return json.loads(err_body), e.code
        except:
            return {"message": err_body}, e.code

def get_file_sha(repo, path):
    """Get SHA of existing file, or None if not found."""
    result, status = github_api("GET", f"/repos/{OWNER}/{repo}/contents/{path}")
    if status == 200:
        return result.get("sha")
    return None

def push_file(repo, path, local_path, message):
    """Push a single file to a repo."""
    with open(local_path, "rb") as f:
        content = base64.b64encode(f.read()).decode()
    
    sha = get_file_sha(repo, path)
    
    data = {
        "message": message,
        "content": content,
    }
    if sha:
        data["sha"] = sha  # Required for updates
    
    result, status = github_api("PUT", f"/repos/{OWNER}/{repo}/contents/{path}", data)
    
    if status in (200, 201):
        return True, result.get("commit", {}).get("html_url", "OK")
    else:
        return False, result.get("message", f"HTTP {status}")

# Verify PAT works
print("=" * 60)
print("Arkos SEO Network - GitHub Deploy")
print("=" * 60)
user_result, user_status = github_api("GET", "/user")
if user_status != 200:
    print(f"ERROR: Invalid PAT or API error: {user_result.get('message', user_status)}")
    sys.exit(1)
print(f"Authenticated as: {user_result.get('login')}")
print()

# Deploy each repo
success_count = 0
total_count = 0

for folder, repo in REPOS.items():
    print(f"\n{'='*60}")
    print(f"Deploying: {repo}")
    print(f"{'='*60}")
    
    for filename in FILES_TO_PUSH:
        local_path = os.path.join(os.path.dirname(__file__), folder, filename)
        if not os.path.exists(local_path):
            print(f"  SKIP: {filename} not found at {local_path}")
            continue
        
        total_count += 1
        print(f"  Pushing {filename}...", end=" ")
        
        ok, msg = push_file(
            repo, filename, local_path,
            f"Update {filename}: fix header nav, rename Chart to Comparison Chart, beautify"
        )
        
        if ok:
            print(f"OK")
            success_count += 1
        else:
            print(f"FAILED: {msg}")

print(f"\n{'='*60}")
print(f"DEPLOY COMPLETE: {success_count}/{total_count} files pushed")
print(f"{'='*60}")

if success_count == total_count:
    print("\nAll files deployed successfully!")
    print("GitHub Pages will rebuild automatically. Changes visible in ~2 minutes.")
    print("\nVerify at:")
    print("  https://cbdreviewhouse.com")
    print("  https://cbdreviewhouse.info")
    print("  https://thecbdreviewers.com")
    print("  https://nanocbdlab.com")
    print("  https://nanocbdrankings.com")
