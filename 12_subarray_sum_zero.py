#!/usr/local/bin/python3

# Find sub arrays with sum 0
mylist = [1, 2, 3, 4, 5]
#mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mylistlen = len(mylist)

for i in range(0, mylistlen):
	# print("i:",i)
	#for j in range(i, mylistlen):
	sub = mylist[i:mylistlen]
		## print (i,j)
	print(sub)