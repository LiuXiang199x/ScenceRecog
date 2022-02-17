f = open("./数据获取/sn_datasets.txt")
data = f.readlines()
f.close()

for i in data:
    print(len(i))