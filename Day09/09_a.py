list_1 = [1,8,10,14]
def square(list_1):
	list_2 = []
	for i in list_1:
		result = i*i
		list_2.insert(list_1.index(i),result)
	return list_2
print(square(list_1))

