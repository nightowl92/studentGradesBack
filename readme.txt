to add packages to requirements.txt:
pip3 freeze > requirements.txt

to migrate:
python3 manage.py makemigrations studentgradesapp
python3 manage.py migrate