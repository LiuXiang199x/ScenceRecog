import os

f1 = open("/home/agent/ScenceRecog/数据获取/datasets/标注图片/pics_url/kitchen_hxy/场景分类_kitchen_hxy(original).txt").readlines()
f2 = open("/home/agent/ScenceRecog/数据获取/datasets/标注图片/pics_url/kitchen_hxy/场景分类_kitchen_hxy.txt", "w")
for item in f1:
    tmp_url = item.split("\t")[0]
    
    f2.writelines(tmp_url+"\n")