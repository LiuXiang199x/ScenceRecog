# coding:utf-8

from fileinput import filename
import os
from pydoc import TextRepr
from re import I
from unittest import result

from cv2 import split


def count_nums(f_path):
    f_name = open(f_path)
    label_dics = {}
    label_names = ['balcony', 'bed_room', 'CrossLook_DoorFrame', 'unknown', 'others', 
                   'blurredimag', 'CrossLook_Door', 'person_leg', 'wall', 'LargeOcclusion', 
                   'table_foot', 'toilet_room', 'protective_fence', 'kitchen', 
                   'drawing_room', 'dining_room', 'test_room', "空", "hallway"]
    for name in label_names:
        label_dics[name] = 0
    datas = f_name.readlines()

    for data in datas:
        data = data.replace("\n", "").replace(" ", "").split("\t")[-1].replace("\n", "")
        label_dics[data] += 1

    return label_dics

if __name__ == "__main__":
    
    result = []
    fin_result = {}
    label_names = ['balcony', 'bed_room', 'CrossLook_DoorFrame', 'unknown', 'others', 
                   'blurredimag', 'CrossLook_Door', 'person_leg', 'wall', 'LargeOcclusion', 
                   'table_foot', 'toilet_room', 'protective_fence', 'kitchen', 
                   'drawing_room', 'dining_room', 'test_room', "空", "hallway"]
    for name in label_names:
        fin_result[name] = 0
    
    
    sub_dir = "/home/agent/ScenceRecog/数据获取/datasets/已分类数据集/Datas2Train"
    fs = os.listdir(sub_dir)
    
    for sub_f in fs:
        if sub_f[-1] == "t":
            tmp_file = os.path.join(sub_dir, sub_f)
            if os.path.isfile(tmp_file):
                result.append(count_nums(tmp_file))
    
    for dic in result:
        for item in label_names:
            fin_result[item] += dic[item]
    # 
    sum = 0
    for item in fin_result.values():
        sum += item
    
    print(fin_result)
    print(sum)