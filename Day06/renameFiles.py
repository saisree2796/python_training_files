import os
os.chdir("D:/Python_training/Day07")
# print(os.getcwd())
#print(os.listdir())
for i in os.listdir():
	path,extn= os.path.splitext(i)
	#print(path)
	name,topic,num = path.split("-")
	print(num)
	# #num =num.strip()[1:].zfill(2)
	# new_name= f"{num}-{name}-{topic}{extn}"
	# os.rename(i,new_name)




