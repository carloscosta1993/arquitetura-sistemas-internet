#!/usr/bin/env python

import library
import pprint
import bottle
from bottle import Bottle, run, debug, request, template
import json

app = Bottle()
bd = library.library("mylib")

@app.route('/')
@bottle.view('index')
def index():
	info = {'title': 'Welcome to the',
			'content': 'LIBRARY',
			}
	return template('index.html', info)

@app.route('/books')
def list_books():
	allbooks = bd.listBooks()
	books = allbooks['books']
	# print books[1]
	# return template('listAll.html', books)
	return allbooks

@app.route('/authors')
def listAuthors():
	allauthors = bd.listAuthors()
	return allauthors


@app.route('/book')
def query_function():
	if len(request.query) == 0:
		return "xpto"
	else:
		for id in request.query:
			bookid = request.query[id]
	return bd.getBook(bookid)

@app.route('/author')
def query_function():
	if len(request.query) == 0:
		return "xpto"
	else:
		for name in request.query:
			author = request.query[name]
	return bd.listBooks(author)

@app.route('/createbook')
def query_function():
	items = []
	if len(request.query) == 0:
		return "xpto"
	else:
		for parameter in request.query:
			print request.query[parameter]
			items.append(request.query[parameter])
	print items
	return bd.addBook(items[2], items[0], items[1])

if __name__=="__main__":
	debug()
	run(app, host='localhost', port=8080, reloader=True)