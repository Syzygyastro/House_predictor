import sys
from house_price_app import db
from house_price_app.models import Event
from house_price_app.schemas import EventSchema
import sqlite3
import json


# Marshmallow Schemas
events_schema = EventSchema(many=True)
event_schema = EventSchema()


def get_events():
    """Function to get all events from the database as objects and convert to json.

    NB: This was extracted to a separate function as it is used in multiple places
    """
    all_events = db.session.execute(db.select(Event)).scalars()
    event_json = events_schema.dump(all_events)
    return event_json

def get_event(row_id):
    db_file = "house_price_app\data\house_prices_&_GDP_prepared.db"
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    query = "SELECT * FROM house_prices WHERE Date = ?"
    cursor.execute(query, (row_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        # Convert row to dictionary
        keys = [description[0] for description in cursor.description]
        row_dict = dict(zip(keys, row))
        # Serialize dictionary as JSON string
        #event = json.dumps(row_dict)
        return row_dict
    else:
        return None
