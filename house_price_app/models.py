from house_price_app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    """Class to represent users who have created a login"""

    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Text, unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)

    def __init__(self, email: str, password: str):
        """
        Create a new User object hashing the plain text password.
        """
        self.email = email
        self.password = generate_password_hash(password)

    def check_password(self, password):
        """Check the plain text password matches the hashed password

        :return Boolean:
        """
        return check_password_hash(self.password, password)

    def __repr__(self):
        """
        Returns the attributes of a User as a string, except for the password
        :returns str
        """
        clsname = self.__class__.__name__
        return f"{clsname}: <{self.id}, {self.email}>"


class Year(db.Model):
    """Paralympic event"""

    __tablename__ = "house_prices"
    Date = db.Column(db.Integer, primary_key=True)
    price_all = db.Column(db.Text, nullable=False)
    price_new = db.Column(db.Integer, nullable=False)
    price_modern = db.Column(db.Text, nullable=False)
    price_old = db.Column(db.Text)
    gdp = db.Column(db.Integer)

    def __repr__(self):
        """
        Returns the attributes of the event as a string
        :returns str
        """
        clsname = self.__class__.__name__
        return f"<{clsname}: {self.Date},{self.price_all}, {self.price_new},\
                  {self.price_modern}, {self.price_old}, {self.gdp}>"
