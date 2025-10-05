import requests

def get_token():
    with open('token.txt') as file:
        return file.read().strip()

# Replace with your GitHub username and personal access token
GITHUB_USERNAME = 'archie-linux'
GITHUB_TOKEN = get_token()

# === CONFIGURATION ===
USE_MANUAL_LIST = False          # Set to True to use manual list instead of fetching
MAKE_PRIVATE = False           # True = make repos private, False = make public

# === Optional manual list ===
MANUAL_REPO_LIST = []

headers = {
    "Accept": "application/vnd.github.v3+json",
    "Authorization": f"token {GITHUB_TOKEN}"
}

def fetch_all_repos(username):
    """Fetch all repository names for the given user."""
    repos = []
    page = 1
    while True:
        url = f"https://api.github.com/user/repos?per_page=100&page={page}"
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f"❌ Failed to fetch repos: {response.status_code} - {response.text}")
            break

        page_data = response.json()
        if not page_data:
            break  # no more pages
        repos.extend([repo["name"] for repo in page_data])
        page += 1
    return repos

def set_repo_visibility(repo_name, private):
    """Set repository visibility to private (True) or public (False)."""
    url = f"https://api.github.com/repos/{GITHUB_USERNAME}/{repo_name}"
    data = {"private": private}
    response = requests.patch(url, json=data, headers=headers)
    
    visibility = "private" if private else "public"
    if response.status_code == 200:
        print(f"✅ Set {repo_name} to {visibility}")
    else:
        print(f"❌ Failed to set {repo_name} to {visibility}: {response.status_code} - {response.text}")

# === Main Logic ===
if USE_MANUAL_LIST:
    repo_list = MANUAL_REPO_LIST
    print(f"📄 Using manual repo list with {len(repo_list)} repositories")
else:
    repo_list = fetch_all_repos(GITHUB_USERNAME)
    print(f"🔍 Fetched {len(repo_list)} repositories from GitHub")

# Apply visibility change
for repo in repo_list:
    set_repo_visibility(repo, MAKE_PRIVATE)
