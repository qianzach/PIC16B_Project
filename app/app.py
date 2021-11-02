from flask import Flask, g, render_template, request

import sqlite3
import click

import random 
import string

app = Flask(__name__)

# Route to home page
@app.route("/")
def main():
    """
    Function to render the home page 
    """
    return render_template('base.html')
