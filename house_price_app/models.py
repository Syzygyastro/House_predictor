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
        '''
        Checks the plain text password and matches it to the hashed password

        Parameters
        ----------
        password: Any
            The password of the user that is hashed
        Returns
        -------
        check_password_hash: Boolean
            function to check if the password matches
        '''
        return check_password_hash(self.password, password)

    def __repr__(self):
        '''
        Returns the attributes of a User as a string, except for the password

        Parameters
        ----------
        self: Self@User
            The attributes of self
        Returns
        -------
        str
            Attributes of the user, not the password
        '''
        clsname = self.__class__.__name__
        return f"{clsname}: <{self.id}, {self.email}>"


class Year(db.Model):
    """House prices"""

    __tablename__ = "house_prices"
    Date = db.Column(db.Integer, primary_key=True)
    price_all = db.Column(db.Text, nullable=False)
    price_new = db.Column(db.Integer, nullable=False)
    price_modern = db.Column(db.Text, nullable=False)
    price_old = db.Column(db.Text)
    gdp = db.Column(db.Integer)

    def __repr__(self):
        '''
        Returns the attributes of the event as a string

        Parameters
        ----------
        self: Self@User
            the attributes of self
        Returns
        -------
        str
            Attributes of the event as a string
        '''
        clsname = self.__class__.__name__
        return f"<{clsname}: {self.Date},{self.price_all}, {self.price_new},\
                  {self.price_modern}, {self.price_old}, {self.gdp}>"
