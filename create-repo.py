import os
import subprocess
import requests

def get_token():
    with open('token.txt') as file:
        return file.read().strip()

GITHUB_USERNAME = "archie-linux"
GITHUB_TOKEN = get_token()

headers = {
    "Accept": "application/vnd.github.v3+json",
    "Authorization": f"token {GITHUB_TOKEN}"
}

def create_remote_repo(repo_name):
    url = "https://api.github.com/user/repos"
    data = {"name": repo_name, "private": False}
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 201:
        print(f"✅ Created remote repo: {repo_name}")
    elif response.status_code == 422:
        print(f"⚠️ Repo already exists: {repo_name}")
    else:
        print(f"❌ Failed to create {repo_name}: {response.status_code} - {response.text}")

def push_repo(repo_path, repo_name):
    os.chdir(repo_path)
    subprocess.run(["git", "remote", "remove", "origin"], stderr=subprocess.DEVNULL)
    remote_url = f"ssh://git@github.com/{GITHUB_USERNAME}/{repo_name}.git"
    subprocess.run(["git", "remote", "add", "origin", remote_url])
    subprocess.run(["git", "branch", "-M", "main"])
    subprocess.run(["git", "push", "-u", "origin", "main"])
    print(f"🚀 Pushed {repo_name} to GitHub")
    os.chdir("..")

def is_git_repo(path):
    return os.path.isdir(os.path.join(path, ".git"))

# Scan all directories in current path
for folder in os.listdir():
    if os.path.isdir(folder) and is_git_repo(folder):
        print(f"\n🔍 Found repo: {folder}")
        create_remote_repo(folder)
        push_repo(folder, folder)

