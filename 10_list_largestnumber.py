#! /usr/local/bin/python3.6

# find largest number in a list

ilist = [int(x) for x in input().split()]

print("## Solution 1 : By sorting and printing last number")
ilist.sort()
print("Largest number is %d" % ilist[len(ilist) - 1])

print("## Solution 2 : Without sort fucntion")
largestNum = 0
for val in ilist:
	if val > largestNum:
		largestNum = val
	
print("Largest number is %d" % largestNum)	