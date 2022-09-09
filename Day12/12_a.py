class Employee():
	def __init__(self,first,last,pay):
		self.first = first
		self.last=last
		self.pay=pay
		self.email = f"{first}{last}@gmail.com"

	def fullname(self):
		return f"{self.first}{self.last}"

	def apply_raise(self):
		self.pay = int(self.pay*1.18)

emp1 = Employee("sai","sree",70000)
print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)
# print(Employee.fullname(emp1))