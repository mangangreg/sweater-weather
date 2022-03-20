# sweater-weather

Not another weather app!

## Components
- Backend flask app
- Postgres Database (AWS RDS)

## Runing the backend
- `flask run`
  - Setup that makes this work:
    - `.flaskenv` has `FLASK_APP=run.py`
    - `run.py` imports the app object `app` from `./app/__init__.py`

## Flask shell
- `flask shell`
- Setup is in [./run.py:make_shell_context](./run.py)


## Frontend
Using Vue 2, Setup using vue webpack [template](https://github.com/vuejs-templates/webpack) (`vue init webpack sweater-weather`)
Logo from https://pixabay.com/vectors/clothes-clothings-pullover-shirt-1294931/
- Runs at localhost:8080

### Running in development mode
``` npm run dev```

### Building

## Todo
- Solidify data models
- Build endpoints for latest weather
- Start on frontend




## Misc
- AWS connection issues, even though set to allow connection from anywhere had to change inbound VPC rules: https://stackoverflow.com/questions/52324170/aws-rds-for-postgresql-cannot-be-connected-after-several-hours
- 