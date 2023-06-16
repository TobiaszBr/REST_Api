# Car owners API

## How to run locally
- Copy the following SECRET_KEY : 
`"django-insecure-=ok6&fsow=(^4(&&$k=45eda5%d37*!s6xf78jx9wz&&g#6h6-"` 
and paste it at `dev_settings.py` (or `prod_settings.py`) instead of 
`config("SECRET_KEY")`
- If you want to use production settings, go to `manage.py` file and change 
`dev_settings` to `prod_settings` at
`os.environ.setdefault("DJANGO_SETTINGS_MODULE", "car_owners.dev_settings")`
- Choose if you want new empty database or one with some data to tests


### Django localhost and database with data
- Create and activate a virtual environment based on requirements.txt file.
Go to Car_owners directory and run `pip install -r requirements.txt` command at terminal
- Copy the following DB_PASSWORD : `"uzRRPett4YE67WC6Bn9C"`
and paste it at `dev_settings.py` (or `prod_settings.py`) instead of 
`config("DB_PASSWORD")`
- Finally, at terminal run `python manage.py runserver`


### Docker and empty database
- To use that way, there is a need to have Docker installed
- Change `DATABASE_WITH_DATA` variable at `dev_settings.py` (or `prod_settings.py`)
to `False`
- At terminal run `docker-compose up -d`


## API

1. Open Swagger view with all possible endpoints and theirs descriptions:
`http://localhost:8000/`

or

2. Open API Root view based on django-rest-framework:
`http://localhost:8000/app/`
