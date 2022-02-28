import os


f = "数据获取/datasets/已分类数据集/test"
f2 = open("数据获取/datasets/已分类数据集/test/new/new.txt", "w")

print(os.listdir(f))
for tmpf in os.listdir(f):
    
    if "txt" in tmpf:
        print("1")
        tmp_data = open(os.path.join(f, tmpf)).readlines()
        
        for datas in tmp_data:
            data = datas.replace(" ", "").replace("\n", "").split("\t")[-1]
            if data in ["bed_room", "toilet_room", "drawing_room", "dining_room", "LargeOcclusion", "wall", "table_foot", "kitchen"]:
                f2.writelines(datas.replace(" ", ""))

f2.close()