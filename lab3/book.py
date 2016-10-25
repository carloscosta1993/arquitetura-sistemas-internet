# -*- coding: utf-8 -*-


class Book:
	def __init__(self,author,title,publication_date,identifier):
		self.author = author
		self.title = title
		self.publication_date = publication_date
		self.identifier = identifier

	def __str__(self):
		return " %s %s %s" % (self.author, self.title, self.publication_date)
