import requests
import imghdr

def download_pics_withURL():
    pic_path = "/home/agent/桌面/sofa/"
    url_file = open("/home/agent/ScenceRecog/数据获取/datasets/标注图片/pics_url/sofa/sofa.txt")
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


def filer_pics_bed():
    url_file_f = open("/home/agent/ScenceRecog/数据获取/datasets/标注图片/pics_url/diningtable/diningtable_filter.txt", "w")
    url_file = open("/home/agent/ScenceRecog/数据获取/datasets/标注图片/pics_url/diningtable/diningtable.txt")
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
                   
                    
filer_pics_bed()