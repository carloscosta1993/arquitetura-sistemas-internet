# [START app]
# -*- coding: utf-8 -*-
import logging
import application
import json
import urllib2
from flask import Flask, render_template, request


app = Flask(__name__)
services = application.Application()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user', methods=['POST'])
def user_page():
    identifier = int(request.form['identifier'])
    if identifier == 0:
        username = 'Admin'
    else:
        username = 'Student'
    data = urllib2.urlopen('https://fenix.tecnico.ulisboa.pt/api/fenix/v1/spaces').read()
    d = json.loads(data)
    for i in d:
        print i
    return data

@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/get_campus', methods=['GET'])
def get_campus():
    data = services.get_campus()
    return data

@app.route('/get_data/<int:id>', methods=['POST'])
def get(id):
    data = services.get_other(id)
    return data




@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/submitted', methods=['POST'])
def submitted_form():
    name = request.form['name']
    email = request.form['email']
    site = request.form['site_url']
    comments = request.form['comments']
    return render_template(
        'submitted_form.html',
        name=name,
        email=email,
        site=site,
        comments=comments)

@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500
# [END app]