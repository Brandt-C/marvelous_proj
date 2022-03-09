#flask routes control what content is shown on what url depending on use

#the gereal structure of a flask route is a function with a decorator
# a decorator adds lines of code that run before/after the decorated func

#our first route:
#goal display the index.html file when user navigates to the base url

#in order to do this we're gonna need a few things
#1. we need access to our app
from app import app
#import the app variable defined in __init___.py

#2. we need the ability to show html file at a specified url
    #render_template func
    #if your route's job is to display an html page---> it's return value should be a call to render_template
from flask import render_template

@app.route('/')  #decorator says: this is a route of the flask app 'app' with the url endpoint '/'
def home():
    print('JIGGLY Jello')
    z=6
    x=908
    print(z+x)
    return render_template('index.html')


#a second route
@app.route('/manu')
def mcfc():
    return render_template('soccer.html')