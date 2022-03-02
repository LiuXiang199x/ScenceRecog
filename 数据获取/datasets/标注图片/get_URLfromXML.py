# coding:utf-8

from fileinput import filename
import os
from pydoc import TextRepr
from re import I
import re
from tkinter.tix import Tree
from unittest import result

from cv2 import split


def find_index(src, key):
    start_pos = 0
    result = []
    for i in range(src.count(key)):
        if start_pos == 0:
            start_pos = src.index(key)
        else:
            start_pos = src.index(key, start_pos+1)
        result.append(start_pos)
        
    return result

def creat_txts(name):
    xml_path = "数据获取/datasets/标注图片/pic_annotation/" + name + "/场景分类_"+name+"（已标注）"
    saveUrl_file = open("数据获取/datasets/标注图片/pics_name/" + name + "/" + name + ".txt", "w")
    saveName_file = open("数据获取/datasets/标注图片/pics_url/" + name + "/" + name + ".txt", "w")
    i = 0
    for tmp_xml in os.listdir(xml_path):
        f1 = os.path.join(xml_path, tmp_xml)
        print(f1)
        ff = open(f1).readlines()
        tmp_result = find_index(ff, '  <object>\n')
        
        door_flag = False
        for i in tmp_result:
            if "door" in ff[i+1]:
                door_flag = True
                break
        
        if not door_flag:
            i += 1
            saveUrl_file.writelines(ff[3].split(">")[1].split("<")[0]+"\n")
            saveName_file.writelines(ff[4].split(">")[1].split("<")[0]+"\n")
            print(i)
    saveName_file.close()
    saveUrl_file.close()




def aa(xml_path):

    i = 0
    for tmp_xml in os.listdir(xml_path):
        i += 1
        f1 = os.path.join(xml_path, tmp_xml)
        # print(f1)
        ff = open(f1).readlines()
        #print(ff)
        tmp_result = find_index(ff, '  <object>\n')
        for i in tmp_result:
            ww = "door" in ff[i+1]
            if ww:
                print(ff)
        