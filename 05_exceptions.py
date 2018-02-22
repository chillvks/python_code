#!/usr/bin/python

try:
	fileobj = open("nfile.txt","w")
	fileobj.write("Text cant be writen")
except IOError:
	print "Execeptionwa : Apni to L lag gai"
else:
	print "This is correct block. But code wont' come here"
	
print "end of the program"