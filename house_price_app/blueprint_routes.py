from house_price_app.utilities import get_years, get_data
from flask import render_template, Blueprint, abort


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
