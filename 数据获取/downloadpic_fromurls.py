import requests

pic_path = "/home/agent/PICCCCCC/"
url_file = open("/home/agent/ScenceRecog/数据获取/datasets/35Wto7paq/pics_url/35_1(start_1).txt")
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

