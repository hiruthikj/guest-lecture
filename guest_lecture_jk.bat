cd "D:\projects\Django\lecture-management"

pipenv install --skip-lock
pipenv run python manage.py collectstatic
pipenv run python manage.py jenkins --enable-coverage
