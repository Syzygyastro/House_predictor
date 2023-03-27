from house_price_app.models import Year
from house_price_app import db, ma


# -------------------------
# Flask-Marshmallow Schemas
# See https://marshmallow-sqlalchemy.readthedocs.io/en/latest/#generate-marshmallow-schemas
# -------------------------


class YearSchema(ma.SQLAlchemyAutoSchema):
    """Marshmallow schema for the attributes of an event class. Inherits all the attributes from the Event class."""

    class Meta:
        model = Year
        include_fk = True
        load_instance = True
        sqla_session = db.session
        include_relationships = True
