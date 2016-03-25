from flask import render_template, Flask, request, url_for, redirect
from app import app

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/reflection')
def reflection():
    return render_template('reflection.html')

@app.route('/collection')
def collection():
    return render_template('collection.html')