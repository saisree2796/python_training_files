# def sampleA():
# 	return "Hello"
# def sampleB():
# 	return "Hi"

# print(sampleA())
# print(sampleB())


# def sample1():
# 	print("Hello")
# def sample2():
# 	print("Hi")
# sample1()
# sample2()

# def Hello_func(greeting,name):
#   return f"{greeting} {name} function run"

# print(Hello_func("Hello","sai"))

# def emp_info(*details):
#  return f"{details} multiple arguments"
# print(emp_info("empID","empName","salary"))

# def emp_info(*args,**kargs):
# 	print(args)    ##prints only args like java,python##
# 	print(kargs)   ##prints key value pairs##
# emp_info("java","python",name="sai",id=1324,salary=46578979)

def emp_info(*args,**kargs):
	return args,kargs   ##prints both args and kargs
print(emp_info("java","python",name="sai",id=1324,salary=46578979))