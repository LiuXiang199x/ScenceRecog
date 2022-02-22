import requests
import imghdr

def download_pics_withURL():
    pic_path = "/home/agent/桌面/bed/"
    url_file = open("/home/agent/ScenceRecog/数据获取/datasets/标注图片/pics_url/bed/bed.txt")
    url_datas = url_file.readlines()

    for data_url in url_datas:
        
        data = data_url.replace("\n","")
        data = data.replace("\t","")
        data = data.split("/")[-1]
        data_url = data_url.replace("\n","")
        data_url = data_url.replace("\t","")
        
        pic = requests.get(data_url)
        f = open(pic_path+data, "wb")
        f.write(pic.content)
        

# res = requests.get(url)
# f = open("test.jpg", "wb")
# f.write(res.content)

# 38 + png
# CRL + JPG


def filer_pics_visulgood(name):
    url_file_f = open("/home/agent/ScenceRecog/数据获取/datasets/标注图片/pics_url/"+name+"/"+name+"_filter.txt", "w")
    url_file = open("/home/agent/ScenceRecog/数据获取/datasets/标注图片/pics_url/"+name+"/"+name+".txt")
    url_datas = url_file.readlines()

    ttt = 0
    for data_url in url_datas:
        data = data_url.replace("\n","")
        data = data.replace("\t","")
        if not "png" in data:
            if data[-6]=="_" or data[-7]=="_" or data[-8]=="_" or data[-9]=="_" or data[-10]=="_" and len(data) < 100:
                url_file_f.writelines(data+"\n")

    for data_url in url_datas:
        data = data_url.replace("\n","")
        data = data.replace("\t","")
        if not "png" in data:            
            if "UP" in data and "calibration" not in data and "rB" not in data:
                 url_file_f.writelines(data+"\n")
                   
                    
def filer_pics_visulbad_notslam(name):
    url_file_f = open("/home/agent/ScenceRecog/数据获取/datasets/标注图片/pics_url/"+name+"/"+name+"_filter_others.txt", "w")
    url_file = open("/home/agent/ScenceRecog/数据获取/datasets/标注图片/pics_url/"+name+"/"+name+".txt")
    url_datas = url_file.readlines()

    for data_url in url_datas:
        data = data_url.replace("\n","")
        data = data.replace("\t","")
        if not "png" in data:            
            if "rB" not in data:
                if "PURCHASE" not in data:
                    if "slam" not in data:
                        if data[-6]!="_" and data[-7]!="_" and data[-8]!="_" and data[-9]!="_" and data[-10]!="_":
                            if "UP" not in data:
                                if "calibration" not in data:
                                    url_file_f.writelines(data+"\n")
                    

str_name = "TV"
filer_pics_visulgood(str_name)
filer_pics_visulbad_notslam(str_name)