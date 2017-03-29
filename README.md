# Project-Item-Catalog-With-Flask
A simple restaurant menu item catalog built with the Flask framework that allows you to update, delete and create new restaurants and menu items.

# Files used in this project
database_setup.py
- File is used to setup the databases using sqlalchemy

lotsofmenus.py
- A python function used to populate the database file once created with database_setup.py file

client_secrets.json
- contains OAuth2 parameters for connection to the external Google+ authorisation protocol

fb_client_secrets.json
- contains OAuth2 parameters for connection to the external Facebook authorisation protocol

project.py
- Contains all definitions for each HTTP request and threads the website together using the Flask framework


# How to run project
1) Run these files in order with python:
  i) database_setup.py
  ii) lotsofmenus.py
  iii) project.py
  
2) Access the item catalog website through http://localhost:5000
