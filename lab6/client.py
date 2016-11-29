#!/usr/bin/env python

import json, urllib2


def main():
 
	
	exit = False
	uri = 'http://localhost:8080/'
	while not exit:
		l = raw_input("add? search? list? quit?")
		l = l.split()
		
		if len(l)==1:
			command = l[0].upper()
			if command=='QUIT':
				exit = True
			elif command == 'ADD':
				l = raw_input('Insert author title and date separated by # :\n')
				processed_line = l.split('#')
				if len(processed_line) == 3:
					req = urllib2.Request(uri + 'createbook?author=' + processed_line[0] + '&title=' + processed_line[2] + '&date=' + processed_line[1])
					req.add_header('Content-Type', 'application/json')
					response = urllib2.urlopen(req)
					pass
			elif command == 'SEARCH':
				l = raw_input('Insert id :\n')
				processed_line = l.split()
				print processed_line[0]
				try:
					if len(processed_line) == 1:
						data = urllib2.urlopen(uri + 'book?id=' + processed_line[0]).read()
						d = json.loads(data)
						print (d)
						pass
				except:
					print urllib2.HTTPError
			elif command == 'LIST':
				l = raw_input('Insert name :\n')
				processed_line = l.split()
				print processed_line[0]
				if len(processed_line) == 1:
					data = urllib2.urlopen(uri + 'author?author=' + processed_line[0]).read()
					d = json.loads(data)
					print (d)
					pass
				else:
					print urllib2.HTTPError
			else:
				pass			
		
		if len(l)==1 and l[0]=='quit':
			exit = True
    
    

if __name__=="__main__":
    main() 
