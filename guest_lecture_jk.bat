cd "D:\projects\Django\lecture-management"

pipenv install --skip-lock
pipenv run python manage.py collectstatic
pipenv run python manage.py jenkins

@REM git remote add heroku https://git.heroku.com/lecture-management.git
@REM git push heroku master -f
@REM heroku ps:scale web=1
@REM heroku run python manage.py migrate


@REM pipenv install -r requirements.txt --skip-lock
@REM pipenv shell
@REM pipenv run python manage.py jenkins --enable-coverage
