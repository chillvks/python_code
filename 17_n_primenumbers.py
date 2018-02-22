#!/usr/local/bin/python3
# calculating n prime numbers

def isPrime(num):
	if num <= 1:
		return False
	else:
		itr = 2
		for itr in range(2, num -1):
			if num % itr == 0:
				return False	
			itr += 1
		return True
				

print("Input how many prime numbers you want to generate")
num = int(input())
# print(isPrime(num))

print("Numbers are : ", num)
mylist = []
key = 2
print(len(mylist))
while len(mylist) <= num -1:
	# print("Inside while len=%d num =%d" %(len(mylist),num))
	if isPrime(key):
		mylist.append(key)
	key += 1

print("Prime numbers are : ", mylist)