# Import all necessary modules:
from flask import Flask, render_template, url_for, request, redirect, flash, jsonify
app = Flask(__name__)

# Import all required sqlalchemy functionality
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Import database_setup classes
from database_setup import Base, Restaurant, MenuItem

# Create session for CRUD operations
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
@app.route('/restaurants')
@app.route('/restaurants/')
def showRestaurants():
    restaurants = session.query(Restaurant).all()
    return render_template('showRestaurants.html', restaurants=restaurants)

@app.route('/restaurants/new', methods=['GET', 'POST'])
def newRestaurant():
    if request.method == 'POST':
        newrestaurant = Restaurant(name=request.form['name'])
        session.add(newrestaurant)
        session.commit()
        return redirect(url_for('showRestaurants'))
    else:
        return render_template('newRestaurant.html')

@app.route('/restaurants/<int:restaurant_id>/edit', methods=['GET', 'POST'])
def editRestaurant(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    if request.method == 'POST':
        editedRestaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
        if request.form['name']:
            editedRestaurant.name = request.form['name']
        session.add(editedRestaurant)
        session.commit()
        return redirect(url_for('showRestaurants'))
    else:
        return render_template('editRestaurant.html', restaurant=restaurant)

@app.route('/restaurants/<int:restaurant_id>/delete', methods=['GET', 'POST'])
def deleteRestaurant(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    if request.method == 'POST':
        deletedRestaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
        session.delete(deletedRestaurant)
        session.commit()
        return redirect(url_for('showRestaurants'))
    else:
        return render_template('deleteRestaurant.html', restaurant=restaurant)

@app.route('/restaurants/<int:restaurant_id>')
@app.route('/restaurants/<int:restaurant_id>/menu')
def showMenu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    menu = session.query(MenuItem).filter_by(restaurant_id=restaurant_id).all()
    return render_template('showMenu.html', restaurant=restaurant, menu=menu)

@app.route('/restaurants/<int:restaurant_id>/menu/new', methods=['GET', 'POST'])
def newMenuItem(restaurant_id, err = None):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    if request.method == 'POST':
        newmenuitem = Restaurant(name=request.form['name'])
        if request.form['name'] and request.form['price'] and request.form['description'] and request.form['course']:
            newmenuitem.name = request.form['name']
            newmenuitem.price = request.form['price']
            newmenuitem.description = request.form['description']
            newmenuitem.course = request.form['course']
        else:
            # error = "Please Complete Form Before Submitting"
            return render_template('newMenuItem.html', restaurant=restaurant)
        session.add(newmenuitem)
        session.commit()
        return redirect(url_for('showMenu', restaurant_id=restaurant))
    else:
        return render_template('newMenuItem.html', restaurant=restaurant)

@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/edit')
def editMenuItem(restaurant_id, menu_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    menuitem = session.query(MenuItem).filter_by(id=menu_id).one()
    return render_template('editMenuItem.html', restaurant=restaurant, menuitem=menuitem)

@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/delete')
def deleteMenuItem(restaurant_id, menu_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    menuitem = session.query(MenuItem).filter_by(id=menu_id).one()

    return render_template('deleteMenuItem.html', restaurant=restaurant, menuitem=menuitem)

# Setup the server
if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host = '0.0.0.0', port=5000)
