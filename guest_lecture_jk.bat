cd "D:\projects\Django\lecture-management"

pipenv install
@REM pipenv install -r requirements.txt --skip-lock
@REM pipenv shell
pipenv run python manage.py jenkins --enable-coverage
