
from flask import Flask
from .user.routes import user


from config import Config
from .models import db, login
from flask_migrate import Migrate


app = Flask(__name__)


app.config.from_object(Config)

app.register_blueprint(user)


db.init_app(app)


from . import routes
from . import models
