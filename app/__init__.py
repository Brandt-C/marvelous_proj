#common things to see here:
#modules/files/classes/packages/functions
#from the flask package that we installed- import the flask object/class

from flask import Flask


#from our config file, import the config class we created
from config import Config


#define/instantiate our flask object. . . Tell the computer that this is a flask app
app = Flask(__name__)

#tell this app how it should be configured -go to config.py file to set this up
app.config.from_object(Config)
# aka configure our flask app from the config object we just wrote

#we need to tell the app where any routes or models exist
    #import the routes file here (must be after the definition and config of app)
from . import routes
    #from the app folder import the routes
