# coding:utf-8

from fileinput import filename
import os
from pydoc import TextRepr
from re import I
from unittest import result

from cv2 import split


def get_txt(f_path):
    f_name = open(f_path)
    f_door_url = open("/home/agent/ScenceRecog/数据获取/datasets/已分类数据集/Datas2Train/已分类url_names/f_door_url.txt", "a")
    f_doorframe_url = open("/home/agent/ScenceRecog/数据获取/datasets/已分类数据集/Datas2Train/已分类url_names/f_doorframe_url.txt", "a")
    f_others_url = open("/home/agent/ScenceRecog/数据获取/datasets/已分类数据集/Datas2Train/已分类url_names/f_others_url.txt", "a")
    f_door_name = open("/home/agent/ScenceRecog/数据获取/datasets/已分类数据集/Datas2Train/已分类url_names/f_door_name.txt", "a")
    f_doorframe_name = open("/home/agent/ScenceRecog/数据获取/datasets/已分类数据集/Datas2Train/已分类url_names/f_doorframe_name.txt", "a")
    f_others_name = open("/home/agent/ScenceRecog/数据获取/datasets/已分类数据集/Datas2Train/已分类url_names/f_others_name.txt", "a")
    
    for item in f_name.readlines():
        item = item.replace("\n", "")
        tmp_url = item.split("\t")[0]
        tmp_name = item.split("\t")[1]
        if tmp_name == 'CrossLook_DoorFrame':
            f_doorframe_name.writelines(tmp_url.split("/")[-1] + "\n")
            f_doorframe_url.writelines(tmp_url+"\n")
    
        if tmp_name == 'CrossLook_Door':
            f_door_name.writelines(tmp_url.split("/")[-1] + "\n")
            f_door_url.writelines(tmp_url+"\n")
    
        if tmp_name == 'others':
            f_others_name.writelines(tmp_url.split("/")[-1] + "\n")
            f_others_url.writelines(tmp_url+"\n")
    
        

if __name__ == "__main__":
    
    result = []
    fin_result = {}
    label_names = ['CrossLook_DoorFrame', 'others', 'CrossLook_Door']
    for name in label_names:
        fin_result[name] = 0
    
    
    sub_dir = "/home/agent/ScenceRecog/数据获取/datasets/已分类数据集/Datas2Train"
    fs = os.listdir(sub_dir)
    
    for sub_f in fs:
        if sub_f[-1] == "t":
            tmp_file = os.path.join(sub_dir, sub_f)
            if os.path.isfile(tmp_file):
                get_txt(tmp_file)
    
