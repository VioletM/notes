## git commit author

```bash
git commit --author="Violetta Mishechkina <email>"
```
## update fork from original project

```bash
git remote add upstream path_to_original_proj 
git fetch upstream
git checkout master
git merge upstream/master
```
## magic
[Split existing commit](https://stackoverflow.com/questions/6217156/break-a-previous-commit-into-multiple-commits) (force push after that)
[Undo git reset](https://stackoverflow.com/questions/2510276/how-to-undo-git-reset)
