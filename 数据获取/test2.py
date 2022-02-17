from operator import imod

# coding:utf-8
import sys
import argparse
import os

datasets_dir = "./数据获取/datasets/originals/"
root = os.listdir(datasets_dir)
file_final = open("txt_final.txt", "a")

def get_file():
    for sub_dir in root:
        tmp_dirs = datasets_dir + sub_dir + "/"
        tmp_gen = os.walk(tmp_dirs)
        for sub_file in tmp_gen:
            for txt_file in sub_file[2]:
                txt_path = tmp_dirs + txt_file

                tmp_file = open(txt_path)
                datas = tmp_file.readlines()
                tmp_file.close()
                for data in datas:
                    file_final.writelines(data)
    file_final.close()

def check():
    ff = open("txt_final.txt")
    datas = ff.readlines()
    i = 0
    for _ in datas:
        i+=1
    print(i)


