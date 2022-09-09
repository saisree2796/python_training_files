#if True:
	#print("Statement is true")
#else:
#	print("statement is false")


#condition = True
#if condition:
#	print("statement is true")
#else:
#	print("statement is false")

a= [23,2,40]
b=[23,2,40]
print(a is b) ###False###
print(a==b)

a1= [1,5,6]
b1= [1,6,5]
print(a1 is b1)  ###False###
print(a1==b1)    ###False###

a2= ["Hi","Hello","Bye"]
b2= ["Hi","Hello","Bye"]
print(a2 is b2)     ###False###
print(a2==b2)

a3 = "Hi,Hello"
b3 = "Hi,Hello"
print(a3 is b3)
print(a3==b3)

a4 = 10
b4 = 10
print(a4 is b4)
print(a4==b4)

a5 = (1,2,3)
b5 = (1,2,3)
print(a5 is b5)
print(a5==b5)

a6 = ("Hi","Hello","Bye")
b6 = ("Hi","Hello","Bye")
print(a6 is b6)
print(a6==b6)

a7 = {12,13,14}
b7 = {12,13,14}
print(a7 is b7)   ###False###
print(a7==b7)

a8 = {"name":"sai","salary":90000}
b8 = {"name":"sai","salary":90000}
print(a8 is b8)   ###False###
print(a8==b8)