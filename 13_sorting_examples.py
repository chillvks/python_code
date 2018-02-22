#!/usr/local/bin/python3

# Bubble Sort : It will compare one element and move largest element in last.
# Help: https://www.tutorialspoint.com/data_structures_algorithms/bubble_sort_algorithm.htm

ilist = [33, 12, 44, 21, 6, 0]


# function to swap the values
def swap(ilist, current):
	tempval = ilist[current]
	ilist[current] = ilist[current+1]
	ilist[current+1] = tempval
	return
	

print("--- Bubble Sort ---")

for x in range(len(ilist) -1, 0, -1):
	for y in range(len(ilist) - 1):
		print("x: ",x)
		print("y: ",y)
		print(ilist)
		if ilist[y] > ilist[y+1]:
			print("Inside loop")
			swap(ilist, y)
			print(ilist)


#print(ilist)