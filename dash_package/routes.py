from flask import render_template, request
from dash_package.network import app

# Create route to home page
@app.server.route('/')
def index():
    return render_template('index.html')

# Create route to networkx dashboard page
@app.server.route('/dash/')
def dashboard():
    return app.index()

# Create route to recommendations page
@app.server.route('/recommendations')
def recommendations():
    return "Under Construction"

