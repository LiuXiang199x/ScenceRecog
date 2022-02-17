# coding: utf-8

file1 = open("./数据获取/sn_5.10-6.8.txt")
file2 = open("./数据获取/sn_6.25-7.8.txt")
file3 = open("./数据获取/sn_9.11-9.30.txt")
file4 = open("./数据获取/sn_12.5-12.19.txt")

datas1 = file1.readlines()
datas2 = file2.readlines()
datas3 = file3.readlines()
datas4 = file4.readlines()

file1.close()
file2.close()
file3.close()
file4.close()

str = ""
for data in datas1:
    data = data.replace("\n", "")
    str = str + data +","
print("datas1: \n", str)

str = ""
for data in datas2:
    data = data.replace("\n", "")
    str = str + data +","
print("datas2: \n", str)

str = ""
for data in datas3:
    data = data.replace("\n", "")
    str = str + data +","
print("datas3: \n", str)

str = ""
for data in datas4:
    data = data.replace("\n", "")
    str = str + data +","
print("datas4: \n", str)