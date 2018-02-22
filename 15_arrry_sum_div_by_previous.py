#!/usr/local/bin/python3
# Array sum after dividing numbers from previous
'''
Input : 3 7 9 10 12 18
Explanation:  3 + 7/3 + 9/7 + 10/9 + 
12/10 + 18/12 = 9 (taking only integer 
part)   
Output : 9

Input : 1 12 24 30 60
Output : 18
'''

myarr = [int(x) for x in input().split()]
arrlen = len(myarr)
itr = 0
final = 0

if arrlen < 1:
	print("Array is empty")
	exit()
else:
	print("array lenght : ",arrlen)

	final = myarr[0]
	itr += 1	
	print("# itr is: ", itr, "final: ", final)
	while itr < arrlen:
		print("itr is: ", itr, "final: ", final)
		final = final + myarr[itr] / myarr[itr-1]
		itr += 1
		

print("Final output is : ",final)	

