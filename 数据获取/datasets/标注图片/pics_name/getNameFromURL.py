import requests
import imghdr

def ff_total(name):
    names_file = open("/home/agent/ScenceRecog/数据获取/datasets/标注图片/pics_name/"+name+"/"+name+".txt", "w")
    url_file = open("/home/agent/ScenceRecog/数据获取/datasets/标注图片/pics_url/"+name+"/"+name+".txt")
    url_datas = url_file.readlines()

    for data_url in url_datas:
        data = data_url.replace("\n","")
        data = data.replace("\t","")
        names_file.writelines(data.split("/")[-1] + "\n")

def ff_filter(name):
    names_file = open("/home/agent/ScenceRecog/数据获取/datasets/标注图片/pics_name/"+name+"/"+name+"_filter.txt", "w")
    url_file = open("/home/agent/ScenceRecog/数据获取/datasets/标注图片/pics_url/"+name+"/"+name+"_filter.txt")
    url_datas = url_file.readlines()

    for data_url in url_datas:
        data = data_url.replace("\n","")
        data = data.replace("\t","")
        names_file.writelines(data.split("/")[-1] + "\n")

def ff_filter_others(name):
    names_file = open("/home/agent/ScenceRecog/数据获取/datasets/标注图片/pics_name/"+name+"/"+name+"_filter_others.txt", "w")
    url_file = open("/home/agent/ScenceRecog/数据获取/datasets/标注图片/pics_url/"+name+"/"+name+"_filter_others.txt")
    url_datas = url_file.readlines()

    for data_url in url_datas:
        data = data_url.replace("\n","")
        data = data.replace("\t","")
        names_file.writelines(data.split("/")[-1] + "\n")

for str_name in ["cabinet", "cupboard", "teatable", "TV", "sofa", "bed"]:
    ff_filter(str_name)
    ff_filter_others(str_name)
