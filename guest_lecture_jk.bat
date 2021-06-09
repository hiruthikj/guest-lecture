cd "D:\projects\Django\lecture-management"

pipenv install
pipenv run python manage.py collectstatic
pipenv run python manage.py jenkins

@REM pipenv install -r requirements.txt --skip-lock
@REM pipenv shell
@REM pipenv run python manage.py jenkins --enable-coverage
