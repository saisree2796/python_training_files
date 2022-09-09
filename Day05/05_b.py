# ## If condition for integers##

# # a = 15
# # b = 15

# # if a==b:
# # 	print(f"The condition is {a}=={b} and it is {a==b}")
# # 	print("The condition is {}=={} and it is {}".format(a,b,a==b))
# # elif a>=b:
# # 	print(f"The condition is {a}>={b} and it is {a>=b}")
# # 	print("The condition is {}>={} and it is {}".format(a,b,a>=b))
# # #elif(a<b):
# # 	#print(f"The condition is {a}<{b} and it is {a<b}")
# # 	#print("The condition is {}<{} and it is {}".format(a,b,a<b))
# # elif a>b:
# # 	print(f"The condition is {a}>{b} and it is {a>b}")
# # 	print("The condition is {}>{} and it is {}".format(a,b,a>b))
# # else:
# # 	print(f"The condition is {a}!={b} and it is {a!=b}")
# # 	print("The condition is {}!={} and it is {}".format(a,b,a!=b))


# ### If condition for strings###
# salary = 50000
# language = "Java"

# if salary == 50000 and language =="Java":
# 	print(f"{language} programming language with a salary of {salary}")
# 	print("{} programming language with a salary of {}".format(language,salary))
# elif salary == 50000 or language=="Python":
# 	print(f"language is not {language} but condition satisfies with salary of {salary}")
# 	print("language is not {} but condition satisfies with salary of {}".format(language,salary))
# elif salary == 50000 and language=="Java":
# 	print(f"Programming language is {language}")
# 	print("Programming language is {}".format(language))
# else:
# 	print(f"None of the conditions satisfies")


# ############
# price = 100223
# has_good_credit= False

# if has_good_credit:
# 	print("Eligible for the loan")
# 	Down_Payment = int(9.5*price)
# 	print(f"Down Payment for the loan is ${Down_Payment}")
# else:
# 	print("As not having enough credit score put down to 20%")
# 	Down_Payment = int(9.5*price)
# 	print(f"Down Payment for the loan is ${Down_Payment}")


list_1 = [1,4,10,2,6]

for i in list_1:
	if i == 10:
		print("Found")
	print(i)