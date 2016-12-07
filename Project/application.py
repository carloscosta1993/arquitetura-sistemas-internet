# -*- coding: utf-8 -*-


import user
import urllib2
import json

class Application:



    def __init__(self):
        admin_user = user.User('Admin', 0)

    def get_campus(self):
        rooms_array = []
        data = urllib2.urlopen('https://fenix.tecnico.ulisboa.pt/api/fenix/v1/spaces').read()
        d = json.loads(data)
        # for name in d:
        #     rooms_array.append({'campus': name['name'].encode('utf-8'), 'id': name['id']})
        return data

    def get_other(self, id_data):
        data = urllib2.urlopen('https://fenix.tecnico.ulisboa.pt/api/fenix/v1/spaces/' + str(id_data)).read()
        return data
