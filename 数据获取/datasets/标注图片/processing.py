# coding:utf-8

from fileinput import filename
import os
from pydoc import TextRepr
from re import I
from unittest import result

from cv2 import split



def creat_txts(xml_path):

    saveUrl_file = open("数据获取/datasets/标注图片/pics_name/bed/bed.txt", "w")
    saveName_file = open("数据获取/datasets/标注图片/pics_url/bed/bed.txt", "w")
    i = 0
    for tmp_xml in os.listdir(xml_path):
        i += 1
        f1 = os.path.join(xml_path, tmp_xml)
        print(f1)
        ff = open(f1).readlines()
        saveUrl_file.writelines(ff[3].split(">")[1].split("<")[0]+"\n")
        saveName_file.writelines(ff[4].split(">")[1].split("<")[0]+"\n")
        print(i)
    saveName_file.close()
    saveUrl_file.close()

toilet_xml_path = "数据获取/datasets/标注图片/pic_annotation/bed/场景分类_bed（已标注）"
creat_txts(toilet_xml_path)

