###tuple### ........... immutable

num = ("sai","sree","vams")
#num[1] = "pall"
print(num)

###sets###

set_1 = {"item1","item2","item3","item3","item1"}
print(set_1)

###Dictionaries###   ..... multiple datatypes

dic_1 = {"name":"sai","salary":65000,"first":"s","last":"v"}
print(dic_1["name"])
print(dic_1.get("name"))
dic_1["email"]="xyz@x.com"
print(dic_1)
dic_1.update({"phoneNumber":7898080,"salary":5668787})
print(dic_1)
del dic_1["name"]
print(dic_1)
dic_1.pop("salary")
print(dic_1)
print(dic_1.items())
print(dic_1.keys())
print(dic_1.values())

for i,v in dic_1.items():
  print(f"{i}---{v}")
