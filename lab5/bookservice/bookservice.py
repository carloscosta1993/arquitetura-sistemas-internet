#!/usr/bin/env python

import library
import pprint
from bottle import Bottle, run, debug
import json

app = Bottle()
bd = library.library("mylib")

 
	
@app.route('/')
def index():
	return "Welcome to the book <b>library</b>"

@app.route('/books')
def listBooks():
	allbooks = bd.listBooks()
	return allbooks

@app.route('/authors')
def listAuthors():
	allauthors = bd.listAuthors()
	return allauthors

@app.route('/authors/')




if __name__=="__main__":
	debug()
	run(app, host='localhost', port=8080, reloader=True)
