from flask import render_template, request

from dash_package.network import app


@app.server.route('/')
def index():
    return render_template('index.html')

@app.server.route('/dash/')
def dashboard():
    return app.index()


@app.server.route('/recommendations')
def recommendations():
    return "Under Construction"

