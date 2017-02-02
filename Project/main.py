# [START app]
# -*- coding: utf-8 -*-
import logging
import application
import json
from google.appengine.ext import ndb
from flask import Flask, render_template


app = Flask(__name__)
services = application.Application()

class Room(ndb.Model):
  name = ndb.StringProperty()
  capacity = ndb.IntegerProperty()

class User(ndb.Model):
    name = ndb.StringProperty()
    identifier = ndb.IntegerProperty()

class Check(ndb.Model):
    user = ndb.StringProperty()
    room = ndb.StringProperty()
    identifier = ndb.IntegerProperty()
    check_type = ndb.StringProperty()

def get_room(identifier):
    user_room = Check.query(Check.identifier == identifier).get()
    print user_room
    if user_room is not None:
        return user_room.room
    else:
        return "None"

@app.route('/checkin/<string:user>/<int:identifier>/<string:room>/<string:check_type>', methods=['POST'])
def checkin(user, identifier, room, check_type):
    check_in = Check(user=user, room=room, identifier=identifier, check_type=check_type)
    c = check_in.put()
    return "Checked-in in room" + room

@app.route('/checkout/<int:identifier>', methods=['POST'])
def checkout(identifier):
    check_out = Check.query(Check.identifier == identifier).get()
    check_out.key.delete()
    return "Checked-out"

@app.route('/who_is_in_the_room/<string:room>', methods=['GET'])
def who_is_in_the_room(room):
    who = []
    data = Check.query(Check.room == room)
    for entry in data:
        who.append(entry.user.encode('utf-8'))
    return json.dumps(who)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<string:username>/<int:identifier>', methods=['GET'])
def user_page(username, identifier):
    room = get_rooms_used()
    rooms = json.loads(room)
    user_room = get_room(identifier)
    return render_template('user.html', username=username, identifier=identifier, rooms=rooms, user_room=user_room)

@app.route('/login/<int:identifier>', methods=['GET', 'POST'])
def login(identifier):
    sign_in = []
    if identifier == 0:
        return "admin"
    else:
        user_identifier = User.query(User.identifier == identifier).get()
        if user_identifier is not None:
            sign_in.append(user_identifier.name.encode('utf-8'))
            sign_in.append(user_identifier.identifier)
            return json.dumps(sign_in)
        else:
            return "None"

@app.route('/register/<string:username>', methods=['POST'])
def register(username):
    aux = 1
    verification = "true"
    qry = User.query()
    record_list = qry.fetch()
    print(record_list)
    if not record_list:
        user = User(name=username, identifier=1)
        load = user.put()
        msg = "SUCCESS! Username: " + username.encode('utf-8') + " Identifier: 1"
    else:
        for k in qry:
            if k.identifier > aux:
                aux = k.identifier
            if k.name.encode('utf-8') == username:
                verification = "false"
        if verification == "true":
            user = User(name=username, identifier=aux+1)
            load = user.put()
            msg = "SUCCESS! Username: " + username + " Identifier: " + str(aux+1)
        else:
            msg = "User already exists! Try another."
    return msg

@app.route('/admin/<int:identifier>', methods=['GET'])
def admin(identifier):
    if identifier == 0:
        rooms = []
        msgs = Room.query()
        for k in msgs:
            rooms.append([k.name.encode('utf-8'), k.capacity])
        return render_template('admin.html', rooms=rooms)
    else:
        return server_error

@app.route('/get_rooms_used', methods=['GET'])
def get_rooms_used():
    ret = ""
    rooms = []
    msgs = Room.query()
    for k in msgs:
        print k
        ret += k.name + "    " + str(k.capacity)
        rooms.append([k.name.encode('utf-8'), k.capacity])
    return json.dumps(rooms)

@app.route('/get_campus', methods=['GET'])
def get_campus():
    data = services.get_campus()
    return data

@app.route('/get_data/<int:id>', methods=['POST'])
def get(id):
    data = services.get_other(id)
    return data

@app.route('/store_data/<string:room>/<int:capacity>', methods=['POST'])
def store(room, capacity):
    p = Room(name=room, capacity=capacity)
    k = p.put()
    p2 = k.get()
    print p2
    return render_template('admin.html')

@app.route('/delete_room/<string:room>',methods=['DELETE'])
def delete_room(room):
    room_to_delete = Room.query(Room.name == room).get()
    check_to_delete = Check.query(Check.room == room)
    room_to_delete.key.delete()
    for entry in check_to_delete:
        entry.key.delete()
    return render_template('admin.html')

@app.route('/occupancy/<string:room>/<string:check>', methods=['POST'])
def occupancy(room, check):
    seats = Room.query(Room.name == room).get()
    if check == "check-in":
        if seats.capacity == 0:
            return json.dumps(seats.capacity)
        else:
            seats.capacity -= 1
            seats.put()
            return json.dumps(seats.capacity)
    else:
        seats.capacity += 1
        seats.put()
        return json.dumps(seats.capacity)


@app.errorhandler(405)
def server_error(e):
    return 'HTTP/1.1 200 OK', 200

@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500
# [END app]