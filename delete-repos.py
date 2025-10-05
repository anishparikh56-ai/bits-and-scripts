import requests

def get_token():
    with open('token.txt') as file:
        return file.read().strip()

# Replace with your GitHub username and personal access token
GITHUB_USERNAME = "archie-linux"
GITHUB_TOKEN = get_token()

# List of repositories you want to delete
REPOSITORIES = []

headers = {
    "Accept": "application/vnd.github.v3+json",
    "Authorization": f"token {GITHUB_TOKEN}"
}

def delete_repo(repo_name):
    url = f"https://api.github.com/repos/{GITHUB_USERNAME}/{repo_name}"
    response = requests.delete(url, headers=headers)
    if response.status_code == 204:
        print(f"🗑️ Deleted: {repo_name}")
    else:
        print(f"❌ Failed to delete {repo_name}: {response.status_code} - {response.text}")

for repo in REPOSITORIES:
    delete_repo(repo)

