from datetime import datetime

from flask_login import AnonymousUserMixin, UserMixin

from util.extensions import bcrypt, db

# @see https://stackoverflow.com/a/37473078
class Role(UserMixin, db.Model):
    """An user capable or not of viewing screens.

    :param str email: email address of user
    :param str password: password for the user
    :param str postal_code: postal code for the user
    :param str role: 'admin', 'plain' or 'guest'

    """
    __table_args__ = {'extend_existing': True}
    __tablename__ = 'roles'
    

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nombre = db.Column(db.String(100))
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)


    def __init__(self,id,nombre):
        """Create instance."""
        db.Model.__init__(self, id=id, nombre=nombre)
  