#!/usr/bin/env python
import socket          
from pickle  import *


s = socket.socket()        
host = socket.gethostname()
port = 12345              
s.connect((host, port))

msg =  s.recv(1024)
t = loads(msg)
print t.x
s.close   