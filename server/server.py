#!/usr/bin/env python
import socket          
from teste import *
from pickle  import *

s = socket.socket()        
host = socket.gethostname()
port = 12345               
s.bind((host, port))    
s.listen(5)                
while True:
   c, addr = s.accept()    
   print 'Connection from', addr

   t = teste()
   print dumps(t)
   c.send(dumps(t))
   c.close()
