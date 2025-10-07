### Bash Profile

### SSH Agent Setup

eval $(ssh-agent)
ssh-add -D
ssh-add ~/.ssh/id_git_rsa
ssh-add ~/.ssh/tech-guides
ssh-add ~/.ssh/bitbucket_key
ssh-add -L

### Git Aliases

alias gadd='git add .'
alias gfix='git commit --amend --no-edit && git push -f # push force
git rebase -i --root --exec "git commit --amend --no-edit --reset-author" # update author
GIT_SEQUENCE_EDITOR="sed -i '' '2,\$s/^pick/squash/'" git rebase -i --root # squash commits

