print 'hello'

x = 34 - 23 # A comment.
y = 'Hello' # Another one.
z = 3.45
if z == 3.45 or y == 'Hello':
 x = x + 1
 y = y + ' World' # String concat.
print x
print y

print "What's your name?"
name = raw_input("> ")
print "What year were you born?"
birthyear = int(raw_input("> "))
print "Hi %s! You are %d years old!" % (name, 2016 - birthyear)

import math
x = 30
if x <= 15 :
 y = x + 15
elif x <= 30 :
 y = x + 30
else :
 y = x
print 'y = ',
print math.sin(y) 

x = 1
while x < 10 :
 print x
 x = x + 1
