#! /usr/bin/python

# My Way of doing it in first shot
mylist = [1, 2, 3, 4, 5, 6, 7]

listlenght = len(mylist)
number = 0

if listlenght > 0:
	for itr in mylist:
		number += itr
else:
	print('Input list is not having any element.')
	exit(0)

print("Average of list is : ",number/listlenght)

## Doing other way, explained in other example

num_of_elm = int(input("Enter number of elements to be added: "))
print num_of_elm
inlist = []

for itr in range(0, num_of_elm):
	inlist.append(int(input('Enter Number: ')))

avg = sum(inlist) / num_of_elm
print('Average is :', avg)
	