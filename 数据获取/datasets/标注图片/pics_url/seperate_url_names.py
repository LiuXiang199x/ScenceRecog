import os

f1 = open("/home/agent/ScenceRecog/数据获取/datasets/标注图片/pics_url/toilet/场景分类_toiletroom_hxy.txt").readlines()
f2 = open("/home/agent/ScenceRecog/数据获取/datasets/标注图片/pics_url/toilet/toiletroom_hxy.txt", "w")
f3 = open("/home/agent/ScenceRecog/数据获取/datasets/标注图片/pics_name/toilet/toiletroom_hxy.txt", "w")

for item in f1:
    tmp_url = item.split("\t")[0]
    
    f2.writelines(tmp_url+"\n")