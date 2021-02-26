Apply changes:
```bash
git pull
python manage.py makemigrations my_app
python manage.py migrate
sudo supervisorctl restart olympiad
```
