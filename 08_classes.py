#! /usr/bin/python

class Employee:
	'This is optional document string'
	
	empCount = 0
	
	def __init__(self, name, salary):
		self.name =  name
		self.salary = salary
		Employee.empCount += 1
		
	def displayCount(self):
		print('Total number of employee: ',Employee.empCount)
	
	def displayEmployee(self):
		print('Name :',self.name,' Salary : ',self.salary)
		


#class Managers:


emp01 = Employee('Vikas', 50000)
emp01.displayCount()
emp01.displayEmployee()
emp02 = Employee('Moh', 80000)
emp02.displayCount()
emp02.displayEmployee()
emp03 = Employee('Reyansh', 50)
emp03.displayCount()
emp03.displayEmployee()

print(Employee.__doc__)
print(emp01.__dict__)
print(Employee.__dict__)