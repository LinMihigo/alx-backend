#!/usr/bin/env python3
"""Task 0
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """Page to route to!
    """
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
