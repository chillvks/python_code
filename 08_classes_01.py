#! /usr/bin/python

class Student:
	perc_raise = 1.05
	
	def __init__(self, first, last, marks):
		self.first_name = first
		self.last_name = last
		self.marks = marks
		self.email = first + '.' + last + '@gmail.com'
	
	def increment(self):
		self.marks = self.marks * Student.perc_raise
		
	def fullname(self):
		print('{} {}'.format(self.first_name, self.last_name))
		
		

class Dumb_Student(Student):
	perc_raise = 1.10
	def increment(self):
		Student.marks = Student.marks * perc_raise	
	def status(self):
		print("I am a dumb student")

std01 = Student('vikas', 'singh', 80)
std01.fullname()
print('Marks: ', std01.marks)
std01.increment()
print('Marks updated: ', std01.marks)

std02 = Dumb_Student('rajesh', 'gupta', 50)
std02.fullname()
print('Marks: ', std02.marks)
std02.increment()
print('Marks updated: ', std02.marks)
std02.status()

#print(help(Dumb_Student))