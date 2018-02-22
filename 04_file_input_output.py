#! /usr/bin/python
import os
# opening and closing file : File operation
print os.getcwd()

fo = open("foo.txt", "w+")
print('File Name: ',fo.name)
print('File Closed or not: ',fo.closed)
print('File opening mode: ', fo.mode)
print('File Softspace flag: ', fo.softspace)

fo.write('First line we are adding in our file\n')
fo.write('Second line we are adding in our file\n')

st =  fo.read(10)
print('file content: ',st)

fo.close()
print('File Closed or not: ',fo.closed)

print '== Second file operation'

# Open a file
fo = open("myfile.txt", "r+")
str1 = fo.read(10)
print "Read String is : ", str1

fo.seek(-10,2)
position = fo.tell()
print 'current file position is : ', position 

str2 = fo.read(10)
print "Read String is : ", str2

# os.rename("myfile.txt", "foo.txt")

# Close opend file
fo.close()

#os.remove("foo.txt")

 