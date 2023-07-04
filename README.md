# Car owners API

## How to run locally
- To run that application properly, installed Docker is required
- Copy the following SECRET_KEY : 
`"django-insecure-=ok6&fsow=(^4(&&$k=45eda5%d37*!s6xf78jx9wz&&g#6h6-"` 
and paste it at `Car_owners/car_owners/prod_settings.py` instead of `config("SECRET_KEY")`
- At terminal go to `Car_owners` directory and run `docker-compose up -d`

## API

1. Open Swagger view with all possible endpoints and theirs descriptions:
`http://localhost:8000/`

or

2. Open API Root view based on django-rest-framework:
`http://localhost:8000/app/`
