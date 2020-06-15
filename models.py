from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

bcrypt= Bcrypt()
db = SQLAlchemy()

class User(db.Model):
    """User."""
    __tablename__ = "users"
    # username - a unique primary key that is no longer than 20 characters.
    # password - a not-nullable column that is text
    # email - a not-nullable column that is unique and no longer than 50 characters.
    # first_name - a not-nullable column that is no longer than 30 characters.
    # last_name - a not-nullable column that is no longer than 30 characters.
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable =False)
    password = db.