cd "D:\projects\Django\lecture-management"

@REM pipenv install
pipenv install -r requirements.txt --skip-lock
@REM pipenv shell
pipenv run python manage.py jenkins --enable-coverage
