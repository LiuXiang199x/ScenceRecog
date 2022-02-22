import requests
import imghdr

def ff():
    names_file = open("/home/agent/ScenceRecog/数据获取/datasets/标注图片/pics_name/bed/bed_filter_others.txt", "w")
    url_file = open("/home/agent/ScenceRecog/数据获取/datasets/标注图片/pics_url/bed/bed_filter_others.txt")
    url_datas = url_file.readlines()

    for data_url in url_datas:
        data = data_url.replace("\n","")
        data = data.replace("\t","")
        names_file.writelines(data.split("/")[-1] + "\n")
                    
ff()
