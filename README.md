

## Set-up

You will need to a Python environment e.g create and activate a venv.

Install the packages from requirements.txt.

Install the app: `pip install -e .`

To run the app:

`python -m flask --app 'house_price_app:run_app()' --debug run`

To run the tests:

`python -m pytest -v tests/`

## Continuous Integration evidence

Passing all 10 tests:

<img width="602" alt="image" src="https://user-images.githubusercontent.com/115084551/230748501-f6833902-fbb4-453e-8609-b25fd769d7c7.png">


Evidence for linting:

<img width="818" alt="image" src="https://user-images.githubusercontent.com/115084551/230748399-76ff8142-4368-413a-80b0-be9423e63e4a.png">


Note: the remaining errors are ignored as the app cannot run if these are removed.
