from proffessor import Proffessor
from enroll import  Enroll

class Course:
	def__init__(self, name, code, max_, min_, proffessor):
	self.name=name
	self.code=code
	self.max=max_
	self.min-min_
	self.proffessors=[] 
	self.enrollments = []

if isinstance (proffessor, Proffessor):
		self.proffessors.append(proffessor)
		elif isinstance(proffessor, list)
		for entry in proffessor:
			if not isinstance(entry,Proffessor):
				raise Error("Invalid Proffessor...")

				self.addresses=address
else
raise Error ("Invalid Proffessor...")

def add_proffessor(self, proffessor):
	if not isinstance(proffessor, Proffessor):
		raise Error("Invalid Proffessor")

		self.proffessor.append(proffessor)

	def add_enrollment(self, Enroll):
		if not isinstance(enroll, Enroll):
			raise Error("Invalid Enroll")

		if leng(enrollments) == self.max:
			raise Error("Cannot enroll, course is full...")

			self.enrollments.append(enroll)

		def is_cancelled(self):
			return len(self.enrollments) <self.min 
