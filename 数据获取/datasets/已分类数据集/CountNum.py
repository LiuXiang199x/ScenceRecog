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
    label_names = ['balcony', 'bed_room ', 'CrossLook_DoorFrame', 'unknown', 'others', 'blurredimag', 'CrossLook_Door', 'person_leg', 'wall', 'LargeOcclusion', 'table_foot', 'toilet_room', 'protective_fence', 'kitchen', 'drawing_room', 'dining_room']
    for name in label_names:
        label_dics[name] = 0
    datas = f_name.readlines()

    for data in datas:
        data = data.split("\t")[-1].replace("\n", "")
        label_dics[data] += 1

    return label_dics

if __name__ == "__main__":
    
    result = []
    fin_result = {}
    label_names = ['balcony', 'bed_room ', 'CrossLook_DoorFrame', 'unknown', 'others', 'blurredimag', 'CrossLook_Door', 'person_leg', 'wall', 'LargeOcclusion', 'table_foot', 'toilet_room', 'protective_fence', 'kitchen', 'drawing_room', 'dining_room']
    for name in label_names:
        fin_result[name] = 0
    
    
    sub_dir = "数据获取/datasets/已分类数据集"
    fs = os.listdir(sub_dir)
    for sub_f in fs:
        if sub_f[-1] == "t":
            tmp_file = os.path.join(sub_dir, sub_f)
            if os.path.isfile(tmp_file):
                result.append(count_nums(tmp_file))
    
    for dic in result:
        for item in label_names:
            fin_result[item] += dic[item]
    
    print(fin_result)