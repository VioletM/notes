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
```bash
[Split existing commit](https://stackoverflow.com/questions/6217156/break-a-previous-commit-into-multiple-commits) (force push after that)
```
