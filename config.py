#set up and organize the app's general configuration
#what secret variable does it need (secret key, database info, mailer info, api keys, etc.)
#what does it's file structure look like?

#we're gonna get some help from os package
import os

#set up the base directory of the entire app - aka help comp figure out our file system and where to find the different pieces of this project
basedir = os.path.abspath(os.path.dirname(__name__))

#config variables setup
class Config:
    """
    set config variables for our entire flask app
    """
    FLASK_APP =os.environ.get('FLASK_APP')
    FLASK_ENV =os.environ.get('FLASK_ENV')
    SECRET_KEY =os.environ.get('SECRET_KEY')

