# Import all necessary modules:
from flask import Flask, render_template, url_for, request, redirect, flash, jsonify
app = Flask(__name__)

# Import all required sqlalchemy functionality
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Import database_setup classes
# from database_setup import Base, Restaurant, MenuItem

# Create session for CRUD operations
# engine = create_engine('sqlite:///restaurantmenu.db')
# Base.metadata.bind = engine
# DBSession = sessionmaker(bind=engine)
# session = DBSession()

@app.route('/')
@app.route('/restaurants')
@app.route('/restaurants/')
def showRestaurants():
    # restaurants = session.query(Restaurant).all()
    return "This page is for displaying all restaurants"

@app.route('/restaurant/new')
def newRestaurant():
    return "This page is for creating a new restaurant"

@app.route('/restaurants/<int:restaurant_id>/edit')
def editRestaurant(restaurant_id):
    return "This page is for editing number %s restaurant"%restaurant_id

@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/edit')
def editMenuItem(restaurant_id, menu_id):
    return "This page is for editing number %s menu item in number %s restaurant"%(menu_id, restaurant_id)

@app.route('/restaurants/<int:restaurant_id>/menu/new')
def newMenu(restaurant_id):
    return "This page is for adding a new menu item to number %s restaurant"%restaurant_id

@app.route('/restaurants/<int:restaurant_id>/delete')
def deleteRestaurant(restaurant_id):
    return "This page is for deleting number %s restaurant"%restaurant_id

@app.route('/restaurants/<int:restaurant_id>')
@app.route('/restaurants/<int:restaurant_id>/menu')
def showMenu(restaurant_id):
    return "This page is for showing the menu from %s restaurant"%restaurant_id

# Setup the server
if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host = '0.0.0.0', port=5000)
