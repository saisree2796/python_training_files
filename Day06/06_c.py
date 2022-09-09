# import index

# list_1 = ["sai","Hello",1,2,10,"hey","Bye"]
# print(index.findIndex(list_1,10))


# import index as ind
# list_1 = ["sai","Hello",1,2,10,"hey","Bye"]
# print(ind.findIndex(list_1,10))

# from index import findIndex,demo
# list_1 = ["sai","Hello",1,2,10,"hey","Bye"]
# print(findIndex(list_1,10))
# demo()

# from index import *
# list_1 = ["sai","Hello",1,2,10,"hey","Bye"]
# print(findIndex(list_1,10))
# demo()

import os
from datetime import datetime
# print(os.getcwd())
#help(os.chdir)
# os.chdir("D:\Python_training\Day05")
# print(os.getcwd())
#print(os.listdir())
#print(os.mkdir("D:\Python_training\Day09"))
#print(help(os.mkdir))
#print(os.rmdir("D:\Python_training\Day09"))
#print(os.rename("D:\Python_training\Day08","D:\Python_training\Hello"))
#print(os.stat("D:\Python_training\Hello"))
m_time = os.stat("index.py").st_mtime
print(datetime.fromtimestamp(m_time))