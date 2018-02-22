#! /usr/bin/python

from datetime import datetime

def myfunc(mylist):
	print('Inside myfunc function')
	mylist.append(4)
	mylist = mylist.append([5,6,7])
	print('Inside Function: ',mylist)
	
nlist = [1,2,3]
print('Starting: ',nlist)	
myfunc(nlist)
print 'Ending: ',nlist

print ('!!! Strating new !!!')
list1 = [1,2,3]
list2 = [5,6,7]
list3 = [(x + y) for x, y in zip(list1, list2)]

print list3

print('-- logging function --')

def log(message, *values):
	if not values:
		print(message)
	else:
		final_msg = ':'.join(str(x) for x in values)
		print('%s: %s' %(message, final_msg))

log('Here is message without values',[])
log('Messgae with values',[1,2,3,4,5])
log('Only Message')						# Without second arguments

mylist = ['one', 'two', 'three', 'four']
log('here is log function', *mylist)

print('---- Checking optional behaviour -----')

def reminder(number , divisor):
	return number % divisor

print reminder(20,3)
print reminder(10,divisor=3)
print reminder(divisor=4, number=10)

print('---> checking for Datetime')

def lognew(message, logtime=None):
	logtime = datetime.now() if logtime is None else logtime
	print('%s :: %s' %(message, logtime)) 	

lognew("Printing log with time1 ")
lognew("Printing log with time2 ")

print('lambda functin exmaple')
sum = lambda arg1,arg2: arg1+arg2
sum_of_two = sum(4,6)
print('sum of two vaues is %d' %sum_of_two)

print('using global variable inside function')
Money = 2000
def AddMoney():
   # Uncomment the following line to fix the code:
   	global Money
	Money = Money + 1

print Money
AddMoney()
print Money