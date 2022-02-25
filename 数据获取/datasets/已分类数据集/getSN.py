# coding:utf-8

from fileinput import filename
from functools import total_ordering
import os
from pydoc import TextRepr
from re import I
from unittest import result

from cv2 import split


def get_snList(f_path):
    
    tmp_f = open(f_path).readlines()
    tmp_sn = []
    
    for tmp_data in tmp_f:
        if "RGB200" in tmp_data:
            tmp_sn.append(tmp_data.split("\t")[0].split("_")[1])
    
    return tmp_sn

total_sn = []

sub_dir = "数据获取/datasets/已分类数据集"
fs = os.listdir(sub_dir)
for sub_f in fs:
    if sub_f[-1] == "t":
        tmp_file = os.path.join(sub_dir, sub_f)
        if os.path.isfile(tmp_file):
            total_sn.extend(get_snList(tmp_file))

sn_file = open("/home/agent/ScenceRecog/数据获取/datasets/已分类数据集/sn_total.txt", "w")
total_sn = set(total_sn)
for i in total_sn:
    sn_file.writelines(i+"\n")
    
sn_file.close()