def outer():
	message = "Hello"
	def inner_func():
		print(message)
		print("Hi")
	return inner_func
my_func=outer()
my_func()