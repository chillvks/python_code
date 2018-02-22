#!/usr/local/bin/python3

# implement insertion sort.

input_arr = [int(x) for x in input().split()]

def insertionsort(arr):
	print("Inside insertion sort")
	for i in range(1, len(arr)):	# run loop from second elements onwards
		key =  arr[i]				# save current position i value in key
		j = i - 1
		
		while j >= 0 and key < arr[j]:
			print("Inside while: j =", j)
			arr[j+1] = arr[j]
			j -= 1
		arr[j +1] = key
	return
		

print("Starting of Array is : ", input_arr)
insertionsort(input_arr)
print("After sorting : ", input_arr)