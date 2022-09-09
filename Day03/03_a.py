messages1 = "Hello,Hi"
print(messages1[0])
print(messages1[-1])
print(len(messages1))
print(messages1[0:2])
print(messages1[0: ])
print(messages1[ :-1])
print(messages1[ : ])

new_message = "fhgjhklghfhgugikhffg hgyf  kjghuiyioo"
print(new_message.index("ik"))
print("hz" in new_message)

messages2 = ["Hello","Hi","Hey"]
print(messages2[0])
print(messages2[-1])
print(len(messages2))
print(messages2[0:2])
print(messages2[0:-1])
print(messages2[0: ])
print(messages2[ :-1])
print(messages2[ : ])

messages2.append("Bye")
print(messages2)
messages2.insert(1,"Bye")
print(messages2)

list_1 = ["sai", "sree", "vams"]
#messages2.append(list_1)
#print(messages2)
#print(messages2[5][0])
messages2.extend(list_1)
print(messages2)

#messages2.remove("Bye")
#print(messages2)

messages2.pop(4)   #takes only integer value
print(messages2)

messages2.pop()    #removes last value by default
print(messages2)


numbers = [20,3,5,35,4,9]
new_num = sorted(numbers)
print(new_num)                    #sorting

numbers.sort(reverse=True)
print(numbers)


### for loop ###

lists = ["sai", "sree", "vams", "kris"]
for names in lists:
	print(names)
for names in enumerate(lists):
	print(names)

### string to lists###

message_string = "hi,there,you?"
print(type(message_string))
message_lists = message_string.split(",")
print(message_lists)

### list to string###
message2_lists = ["Hi", "there", "you"]
print(type(message2_lists))
messages2_string = "|".join(message2_lists)
print(messages2_string)

