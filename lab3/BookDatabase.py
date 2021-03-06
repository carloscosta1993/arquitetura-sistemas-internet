#!/usr/bin/env python
          
import book
import pickle


class BookDatabase:

    def __init__(self, name):
        self.name = name
        try:
            dataBaseFile = open('bd_dump'+name, 'rb')
            self.biblioteca = pickle.load(dataBaseFile)
            dataBaseFile.close()
        except IOError:
            self.biblioteca = {}

    def insertBook(self, author, title, year):
        identifier = len(self.biblioteca)
        self.biblioteca[identifier] = book.Book(author, title, year, identifier)
        dataBaseFile = open('bd_dump'+self.name, 'wb')
        pickle.dump(self.biblioteca, dataBaseFile)
        dataBaseFile.close()

    def listBooks(self, name):
        ret_value = []
        for books in self.biblioteca.values():
            if books.author == name:
                ret_value.append( (books.identifier, books.title))
        return ret_value

    def searchBook(self, identifier):
        return self.biblioteca[identifier]

