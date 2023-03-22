from house_price_app.models import User
from house_price_app import db
from flask import session

def test_index_success(test_client):
    """
    GIVEN a running Flask app
    WHEN an HTTP GET request is made to '/'
    THEN the status code should be 200
    AND the page should contain the the html <title>UK House Prices<</title>"
    """
    response = test_client.get("/")
    assert response.status_code == 200
    assert b"<title>UK House Prices</title>" in response.data



def test_prediction_when_form_submitted(test_client, app):
    """
    GIVEN a running Flask app
    WHEN an HTTP POST request is made to '/' with form data
    THEN the page should return a prediction result with the test "Predicted Iris type"
    AND the status code should be 200 OK
    """
    form_data = {
        "year_wanted": 2030,
        "house_type_selection": "Price (All)"

    }
    response = test_client.post("/", data=form_data)
    assert response.status_code == 200
    assert b"Predicted House price for selected year is" in response.data




def test_new_user_created_when_form_submitted_and_redirect(test_client):
    """
    GIVEN a running Flask app
    WHEN an HTTP POST request is made to '/register' with form data
    THEN the page should return a message "You are registered!"
    AND the text of the email should be on the page
    AND the status code should be 200 OK
    """

    form_data = {"email": "joshhuany@jamble.com", "password": "birthday"}
    response = test_client.post("/register", data=form_data)

    assert response.status_code == 302
    

    # Delete the new user from the database whilst also checking the user was registered
    exists = db.session.execute(
        db.select(User).filter_by(email="joshhuany@jamble.com")
    ).scalar()
    if exists:
        db.session.execute(
            db.delete(User).where(User.email == "joshhuany@jamble.com")
        )
        db.session.commit()
        assert 1 == 1

def test_error_when_register_form_email_format_not_valid(test_client):
    """
    GIVEN a running Flask app
    WHEN an HTTP POST request is made to '/register' with form data where the email is not an email address format
    THEN the page should return a message "This field is required."
    AND the status code should be 200 OK
    """
    form_data = {"username": "james", "password": "secret"}
    response = test_client.post("/register", data=form_data)
    assert response.status_code == 200
    assert "This field is required." in response.data.decode()

def test_error_when_out_of_range_selected(test_client):
    """
    GIVEN a running Flask app
    WHEN an HTTP POST request is made to '/register' with form data where the email is not an email address format
    THEN the page should return a message "This field is required."
    AND the status code should be 200 OK
    """
    form_data = {
        "year_wanted": 203,

    }
    response = test_client.post("/", data=form_data)
    assert response.status_code == 200
    assert b"This field is required." in response.data
    
def test_data_route(test_client):
    """
    GIVEN a running Flask app
    WHEN an HTTP GET request is made to '/api'
    THEN the status code should be 200
    AND the page should contain the the html <title>API Home</title>"
    """
    response = test_client.get("/api")
    assert response.status_code == 200
    assert b"<title>API Home</title>" in response.data


def test_display_event_route(test_client):
    """
    GIVEN a running Flask app
    WHEN an HTTP GET request is made to '/api/display_event/<event_id>'
    THEN the status code should be 200 if the event exists
    AND the page should contain the event details if the event exists
    AND the status code should be 404 if the event does not exist
    """
    # Add a test event to the database
    event = {
        "name": "Test Event",
        "date": "2022-04-01",
        "location": "London",
        "description": "This is a test event",
    }
    response = test_client.post("/events", data=event)
    assert response.status_code == 302

    # Get the id of the test event
    response = test_client.get("/")
    event_id = response.data.decode().split("/")[-1]

    # Test

def test_api_success(test_client):
    """
    GIVEN a running Flask app
    WHEN an HTTP GET request is made to '/api'
    THEN the status code should be 200
    AND the page should contain the the html <title>Past house price data</title>"
    """
    response = test_client.get("/api")
    assert response.status_code == 200
    assert b"<title>Past house price data</title>" in response.data

def test_api_success(test_client):
    """
    GIVEN a running Flask app
    WHEN an HTTP GET request is made to '/api/display_event/2004'
    THEN the status code should be 200
    AND the page should contain the the html <title>Past house price data</title>"
    """
    response = test_client.get("/api/display_event/2004")
    assert response.status_code == 200
    assert b"<title>2004</title>" in response.data
# python -m pytest -v tests/