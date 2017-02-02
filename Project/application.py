# -*- coding: utf-8 -*-


import urllib2

class Application:

    def get_campus(self):
        data = urllib2.urlopen('https://fenix.tecnico.ulisboa.pt/api/fenix/v1/spaces').read()
        return data

    def get_other(self, id_data):
        data = urllib2.urlopen('https://fenix.tecnico.ulisboa.pt/api/fenix/v1/spaces/' + str(id_data)).read()
        return data
