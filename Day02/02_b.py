#Arithmetic operators
# "+" operator

a=10
b=20
addition = a+b
print("The result of '{}'+'{}' is '{}'".format(a,b,addition))
print(f"The result of '{a}'+'{b}' is '{addition}'")

# "-" operator

subtraction = a-b
print("The result of '{}'-'{}' is '{}'".format(a,b,subtraction))
print(f"The result of '{a}'-'{b}' is '{subtraction}'")

# "*" operator

multiplication = a*b
print("The result of '{}'*'{}' is '{}'".format(a,b,multiplication))
print(f"The result of '{a}'*'{b}' is '{multiplication}'")

# "/" operator

division = a/b
print("The result of '{}'/'{}' is '{}'".format(a,b,division))
print(f"The result of '{a}'/'{b}' is '{division}'")

# "%" operator

modulus = a%b
print("The result of '{}'%'{}' is '{}'".format(a,b,modulus))
print(f"The result of '{a}'%'{b}' is '{modulus}'")

# "**" operator, If  integer is "+" then it will ignore digits after decimal but if it i "-"
#then it will be floored i.e., rounded

exponent = a**b
print("The result of '{}'**'{}' is '{}'".format(a,b,exponent))
print(f"The result of '{a}'**'{b}' is '{exponent}'")

# "//" operator

floor_division = a//b
print("The result of '{}'//'{}' is '{}'".format(a,b,floor_division))
print(f"The result of '{a}'//'{b}' is '{floor_division}'")
