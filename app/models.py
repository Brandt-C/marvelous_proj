

from enum import unique
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from datetime import datetime, timezone
from werkzeug.security import generate_password_hash
from uuid import uuid4
from secrets import token_hex

from flask_login import LoginManager, UserMixin

login = LoginManager()

@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):
    id = db.Column(db.String(50), primary_key=True)
    username = db.Column(db.String(15), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    password = db.Column(db.String(250), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.now(timezone.utc))

    def __init__(self, username, email, password, first_name= "", last_name = ""):
        self.username =username
        self.email = email.lower()
        self.first_name = first_name
        self.last_name = last_name
        self.password = generate_password_hash(password)
        self.id = str(uuid4())

# Marvel Character Model should include the following fields:
# - id (Integer)
# - name (String)
# - description (String)
# - comics_appeared_in (Integer)
# - super_power (String)
# - date_created (DateTime w/ datetime.utcnow)

class Char(db.Model):
    id = db.Column(db.String(50), primary_key=True)
    s_name = db.Column(db.String(75), unique=True, nullable=False)
    name = db.Column(db.String(75))
    description = db.Column(db.String(255))
    comic_appearances = db.Column(db.String(150))
    super_power = db.Column(db.String(200))
    equipment = db.Column(db.String(150))
    date_created = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    contributor = db.Column(db.String(50))

    def __init__(self, dict):
        self.id = str(uuid4)
        self.s_name = dict['s_name'].title()
        self.name = dict['name'].title()
        self.description = dict['description']
        self.comic_appearances = dict['comic_appearances']
        self.super_power = dict['super_power']
        self.equipment = dict['equipment']
        self.contributor = dict['contributor']

    def to_dict(self):
        return {
            'id':self.id,
            's_name': self.s_name,
            'name' : self.name,
            'description' : self.description,
            'comic_appearances' : self.comic_appearances,
            'super_power' : self.super_power,
            'equipment' : self.equipment,
            'contributor' : self.contributor
        }

    def from_dict(self, dict):
        if dict.get('s_name'):
            self.s_name = dict['s_name'].title()
        if dict.get('name'):
            self.s_name = dict['name'].title()
        if dict.get('description'):
            self.description = dict['description']
        if dict.get('comic_appearances'):
            self.comic_appearances = dict['comic_appearances']
        if dict.get('super_power'):
            self.super_power = dict['super_power']
        if dict.get('equipment'):
            self.equipment = dict['equipment']
        
        
        


        