from course import course
from student import Student
from datetime import datetime

class Enroll:

	def__init__(self, student, course):
	if not isinstance(student, Student):
		raise Error("Invalid Student...")

	if not isinstance(course, Course):
		raise Error("Invalid course...")

	self.student = student
	self.course = course
	self.grade =None
	self.date =datetime.now()
