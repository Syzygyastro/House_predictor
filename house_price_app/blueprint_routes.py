from house_price_app.utilities import get_event, get_events
from house_price_app.models import Event
from house_price_app.schemas import EventSchema
from flask import render_template, Blueprint, abort, current_app as app
# Marshmallow Schemas
events_schema = EventSchema(many=True)
event_schema = EventSchema()



# Define the Blueprint
main_bp = Blueprint("main", __name__)
@main_bp.route("/api")
def data():
    """Returns the home page"""
    response = get_events()
    return render_template("api_index.html", event_list=response)


@main_bp.route("/api/display_event/<event_id>")
def display_event(event_id):
    """Returns the event detail page"""
    ev = get_event(event_id)
    if ev:
        return render_template("event.html", event=ev)
    else:
        abort(404)
