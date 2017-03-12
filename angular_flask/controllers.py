import os

from flask import Flask, request, Response
from flask import render_template, url_for, redirect, send_from_directory
from flask import send_file, make_response, abort

from angular_flask import app

# routing for API endpoints, generated from the models designated as API_MODELS
#from angular_flask.core import api_manager

# routing for basic pages (pass routing onto the Angular app)
@app.route('/')
@app.route('/mission')
@app.route('/programs')
@app.route('/people')
def basic_pages(**kwargs):
    return make_response(open('angular_flask/templates/index.html').read())

# special file handlers and error handlers
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'img/favicon.ico')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
