
# Github project workflow

connect local folder to github:
git init

Create own local branch to work on:
git checkout -b sem_local_develop
Switch between branches:
git checkout sem_local_develop

Create remote branch:
git remote add sem_remote_develop https://github.com/emielpost/CSS.git
Push you local updates to the remote github branch:
1. First select what to commit to the remote branch, then commit (in this case the entire dir):
current_dir=$( cd -P -- "$(dirname -- "$(command -v -- "$0")")" && pwd -P )
print $current_dir
2. git add $current_dir
3. git commit -m "Default"
Now do the push to remote branch:
git push sem_remote_develop sem_local_develop



# other handy github
Add entire local repos and commit and push all at once:
git add . && git commit -am "update_script" && git push sem_remote_develop sem_local_develop

To retrieve the remote branch from any location
git fetch sem_remote_develop




If you want to merge your update to the master branch, then merge the remote master and local branch
git merge master/sem_remote_develop