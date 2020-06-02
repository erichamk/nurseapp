del db.sqlite3
wsl rm /mnt/c/Users/Erich/PycharmProjects/swnat/nurseapp/migrations/00*
python manage.py makemigrations
python manage.py migrate
REM manage.py createsuperuser
manage.py loaddata db.json

REM manage.py dumpdata --exclude auth.permission --exclude contenttypes --exclude admin.logentry > db.json