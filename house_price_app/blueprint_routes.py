from house_price_app.utilities import get_years, get_data
# from house_price_app.models import Year
# from house_price_app.schemas import EventSchema
from flask import render_template, Blueprint, abort, current_app as app
# Marshmallow Schemas
# events_schema = EventSchema(many=True)
# event_schema = EventSchema()



# Define the Blueprint
main_bp = Blueprint("main", __name__)
@main_bp.route("/api")
def data():
    """Returns the home page"""
    response = get_years()
    return render_template("api_index.html", year=response)


@main_bp.route("/api/display_years/<year>")
def display_event(year):
    """Returns the event detail page"""
    data = get_data(year)
    if data:
        return render_template("data_output.html", data=data)
    else:
        abort(404)
