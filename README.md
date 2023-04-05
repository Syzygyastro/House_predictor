

## Set-up

You will need to a Python environment e.g create and activate a venv.

Install the packages from requirements.txt.

Install the app: `pip install -e .`

To run the app:

`python -m flask --app 'house_price_app:run_app()' --debug run`

To run the tests:

`python -m pytest -v tests/`
