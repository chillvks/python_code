#! /usr/local/bin/python3.6

'''
There is a list with odd/even numbers. place all even numbers in left and odd in right
'''
ilist = [int(x) for x in input().split()]

print(ilist)
print(len(ilist))

start = 0
end = len(ilist) -1

# function to swap the values
def swap(ilist, start, end):
	tempval = ilist[start]
	ilist[start] = ilist[end]
	ilist[end] = tempval
	return

# loop for checking values. From start if find any even replace is with last.		
for i in ilist:
	if start > end:
		break
	print("start = %d end = %d" % (start, end))
	if i % 2 == 0:
#		print(i)
		# traversing last pointer from back to front till getting even odd number
		while True:
			if end <= start:
				break
			elif ilist[end] % 2 == 0:
				end -= 1
			else:
				break
		
		swap(ilist, start, end)
		
		start += 1
	else:
		start += 1
print(ilist)
		
	
	