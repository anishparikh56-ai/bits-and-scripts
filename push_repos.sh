#!/bin/bash

# Script to create remote repositories and push all git repos in current directory
# Requires GitHub CLI (gh) to be installed and authenticated

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Check if gh CLI is installed
if ! command -v gh &> /dev/null; then
    echo -e "${RED}Error: GitHub CLI (gh) is not installed.${NC}"
    echo "Install it from: https://cli.github.com/"
    exit 1
fi

# Check if authenticated
if ! gh auth status &>/dev/null; then
    echo -e "${RED}Error: Not authenticated with GitHub CLI.${NC}"
    echo "Run: gh auth login"
    exit 1
fi

# Get GitHub username
GH_USER=$(gh api user -q .login)

echo "========================================="
echo "Creating remotes and pushing repositories..."
echo "GitHub User: $GH_USER"
echo "========================================="
echo ""

# Counter for statistics
total=0
success=0
skipped=0
failed=0
created=0

# Loop through all directories in current directory
for dir in */; do
    # Remove trailing slash
    dir=${dir%/}
    
    # Check if it's a git repository
    if [ -d "$dir/.git" ]; then
        ((total++))
        echo -e "${YELLOW}Processing: $dir${NC}"
        
        # Change to the directory
        cd "$dir" || continue
        
        # Check if there are any commits
        if ! git rev-parse HEAD &>/dev/null; then
            echo -e "${RED}  ✗ No commits yet, skipping${NC}"
            ((skipped++))
            cd ..
            echo ""
            continue
        fi
        
        # Get current branch
        branch=$(git branch --show-current)
        
        # Check if remote exists and is accessible
        remote_exists=false
        if git remote get-url origin &>/dev/null; then
            # Test if we can actually access it
            if git ls-remote origin &>/dev/null; then
                remote_exists=true
                echo -e "${GREEN}  ✓ Remote exists and is accessible${NC}"
            else
                echo -e "${YELLOW}  ⚠ Remote configured but not accessible, removing...${NC}"
                git remote remove origin
            fi
        fi
        
        # Create remote if it doesn't exist or isn't accessible
        if [ "$remote_exists" = false ]; then
            echo -e "${BLUE}  → Checking if repository exists on GitHub...${NC}"
            
            # Check if repo exists on GitHub
            if gh repo view "$GH_USER/$dir" &>/dev/null; then
                echo -e "${GREEN}  ✓ Repository exists on GitHub, adding remote${NC}"
                git remote add origin "https://github.com/$GH_USER/$dir.git"
            else
                echo -e "${BLUE}  → Creating remote repository: $dir${NC}"
                
                # Create repository on GitHub (change --private to --public for public repos)
                if gh repo create "$dir" --private --source=. --remote=origin --push=false; then
                    echo -e "${GREEN}  ✓ Remote repository created${NC}"
                    ((created++))
                    # Wait a moment for GitHub to fully create the repo
                    sleep 2
                else
                    echo -e "${RED}  ✗ Failed to create remote repository${NC}"
                    ((failed++))
                    cd ..
                    echo ""
                    continue
                fi
            fi
        fi
        
        # Push to remote
        echo -e "${BLUE}  → Pushing $branch to origin${NC}"
        if git push -u origin "$branch" 2>&1 | grep -v "^remote:"; then
            echo -e "${GREEN}  ✓ Successfully pushed $branch${NC}"
            ((success++))
        else
            echo -e "${RED}  ✗ Failed to push $branch${NC}"
            ((failed++))
        fi
        
        # Return to parent directory
        cd ..
        echo ""
    fi
done

# Print summary
echo "========================================="
echo "Summary:"
echo "  Total repositories: $total"
echo -e "  ${BLUE}Created: $created${NC}"
echo -e "  ${GREEN}Successful pushes: $success${NC}"
echo -e "  ${YELLOW}Skipped: $skipped${NC}"
echo -e "  ${RED}Failed: $failed${NC}"
echo "========================================="
