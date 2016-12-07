# -*- coding: utf-8 -*-
class User:
    def __init__(self, username, identifier):
        self.username = username
        self.id = identifier

    def __str__(self):
        return "%s" % self.username
