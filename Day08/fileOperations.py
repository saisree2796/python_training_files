# import csv

# with open("emp_info.csv","r")as rf:
# 	csv_reader= csv.reader(rf)
# 	with open("new_emp_info.csv","w")as wf:
# 		csv_writer= csv.writer(wf)
# 		for line in csv_reader:
# 			csv_writer.writerow(line)


# with open("sample.txt","r") as rf:
# 	for line in rf:
# 		print(line,end="")
# rf.close()

# with open("image.png","rb") as r:
# 	with open("new_image.png","wb") as w:
# 		for line in r:
# 			w.write(line)
# r.close()

import 
with open("excel_data.xlsx","r")as rf:
	with open("new_excel_data.xlsx","w")as wf:
		for line in rf:
			wf.write(line)
