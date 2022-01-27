from distutils import text_file
import os
import sys
import numpy as np

def get_Cmatrix(txt_path):

    test_data = txt_path
    class_name = ['bed_room', 'dining_room', 'drawing_room', 'toilet_room', 'others']
    result = {}
    result_bedroom = {"0":0, "1":0, "2":0, "3":0, "4":0}
    result_diningroom = {"0":0, "1":0, "2":0, "3":0, "4":0}
    result_drawingroom = {"0":0, "1":0, "2":0, "3":0, "4":0}
    result_toiletroom = {"0":0, "1":0, "2":0, "3":0, "4":0}
    result_others = {"0":0, "1":0, "2":0, "3":0, "4":0}

    for item in test_data:
        
        tmp, class_predict = item.split(" ")
        class_label, _ = tmp.split("/")
        class_predict = class_predict.replace("\n", "")
        
        if class_label == 'bed_room':
            if class_predict == "0":
                result_bedroom["0"] += 1
            elif class_predict == "1":
                result_bedroom["1"] += 1
            elif class_predict == "2":
                result_bedroom["2"] += 1
            elif class_predict == "3":
                result_bedroom["3"] += 1
            elif class_predict == "4":
                result_bedroom["4"] += 1
            
        elif class_label == 'dining_room':
            if class_predict == "0":
                result_diningroom["0"] += 1
            elif class_predict == "1":
                result_diningroom["1"] += 1
            elif class_predict == "2":
                result_diningroom["2"] += 1
            elif class_predict == "3":
                result_diningroom["3"] += 1
            elif class_predict == "4":
                result_diningroom["4"] += 1
                
        elif class_label == 'drawing_room':
            if class_predict == "0":
                result_drawingroom["0"] += 1
            elif class_predict == "1":
                result_drawingroom["1"] += 1
            elif class_predict == "2":
                result_drawingroom["2"] += 1
            elif class_predict == "3":
                result_drawingroom["3"] += 1
            elif class_predict == "4":
                result_drawingroom["4"] += 1
            
        elif class_label == 'others':
            if class_predict == "0":
                result_others["0"] += 1
            elif class_predict == "1":
                result_others["1"] += 1
            elif class_predict == "2":
                result_others["2"] += 1
            elif class_predict == "3":
                result_others["3"] += 1
            elif class_predict == "4":
                result_others["4"] += 1
            
        elif class_label == 'toilet_room':
            if class_predict == "0":
                result_toiletroom["0"] += 1
            elif class_predict == "1":
                result_toiletroom["1"] += 1
            elif class_predict == "2":
                result_toiletroom["2"] += 1
            elif class_predict == "3":
                result_toiletroom["3"] += 1
            elif class_predict == "4":
                result_toiletroom["4"] += 1
    
    result['bed_room'] = result_bedroom
    result['dining_room'] = result_diningroom
    result['drawing_room'] = result_drawingroom
    result['toilet_room'] = result_toiletroom
    result['others'] = result_others
    
    return result

result = get_Cmatrix(txt_path=open(os.getcwd() + "/" + "1111111.txt"))
print(result)

# 'bed_room': {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0},  字典里对应的key “0”，“1”， 不是序号，而是txt中模型的实际预测0-4
"""
{'bed_room': {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0}, 
'dining_room': {'0': 16, '1': 168, '2': 11, '3': 16, '4': 8}, 
'drawing_room': {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0}, 
'toilet_room': {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0}, 
'others': {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0}}
"""