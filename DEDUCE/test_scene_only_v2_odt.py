# python test_scene_only_v2.py --dataset=data --envtype=home
# python test_scene_only.py --dataset=vpc --hometype=home1 --floortype=data_1

# Prediction for Scene_Only model
#
# by Anwesan Pal

import argparse
import torch
from torch.autograd import Variable as V
import torchvision.models as models
from torchvision import transforms as trn
from torch.nn import functional as F
import os
from PIL import Image
from config_v2 import places_dir,sun_dir,vpc_dir,home_data_dir
from openpyxl import Workbook


parser = argparse.ArgumentParser(description='DEDUCE Scene_Only Evaluation')
parser.add_argument('--dataset',default='places',help='dataset to test')
parser.add_argument('--hometype',default='home1',help='home type to test')
parser.add_argument('--floortype',default='data_0',help='data type to test')
parser.add_argument('--envtype',default='home',help='home or office type environment')

print(torch.cuda.is_available())

global args
args = parser.parse_args()

# th architecture to use
arch = 'resnet18'

# load the pre-trained weights
model_file = '{}_best_{}.pth.tar'.format(arch,args.envtype)

model = models.__dict__[arch](num_classes=5)
checkpoint = torch.load(model_file, map_location=lambda storage, loc: storage)
state_dict = {str.replace(k,'module.',''): v for k,v in checkpoint['state_dict'].items()}
model.load_state_dict(state_dict)
model.eval()


# load the image transformer
centre_crop = trn.Compose([
        trn.Resize((256,256)),
        trn.CenterCrop(224),
        trn.ToTensor(),
        trn.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

# load the class label
file_name = 'categories_data_{}.txt'.format(args.envtype)

classes = list()
with open(file_name) as class_file:
    for line in class_file:
        classes.append(line.strip().split(' ')[0][3:])
classes = tuple(classes)

if(args.dataset == 'places'):
    data_dir = places_dir + '/places365_standard_{}'.format(args.envtype)
    valdir = os.path.join(data_dir, 'val')
elif(args.dataset == 'sun'):
    data_dir = sun_dir
    valdir = os.path.join(data_dir, 'test')
elif(args.dataset == 'vpc'):
    data_dir = vpc_dir
    home_dir = os.path.join(data_dir, 'data_'+args.hometype)
    valdir = os.path.join(home_dir,args.floortype)
if(args.dataset == 'data'):
    data_dir = home_data_dir
    valdir = os.path.join(data_dir, 'val')

accuracies_list = []
predicted_count = torch.zeros(5,3)

xlsx_path = "/home/agent/ScenceRecog/DEDUCE/111111.xlsx"
wb = Workbook()
ws = wb.active

for class_name in os.listdir(valdir):
    correct, count = 0, 0

    if class_name == 'bed_room':
        class_id = 0
    elif class_name == 'dining_room':
        class_id = 1
    elif class_name == 'drawing_room':
        class_id = 2
    elif class_name == 'others':
        class_id = 3
    elif class_name == 'toilet_room':
        class_id = 4

    for img_name in os.listdir(os.path.join(valdir,class_name)):
        img_dir = os.path.join(valdir,class_name,img_name)
        img = Image.open(img_dir)
        input_img = V(centre_crop(img).unsqueeze(0))

        # forward pass
        logit = model.forward(input_img)
        h_x = F.softmax(logit, 1).data.squeeze()
        print("----------")
        print(h_x)
        probs, idx = h_x.sort(0, True)
        
        # ????????????????????????
        pic_path = "=HYPERLINK(" + "\"" + "/home/agent/ScenceRecog/DEDUCE/data/val/" + class_name + "/" + img_name + "\"" + ")"
        ws.append([pic_path, int(idx[0])])  
        
        if classes[idx[0]] == class_name:
            correct+=1
            predicted_count[idx[0], 0] += 1
        if classes[idx[0]] == 'bed_room':
            predicted_count[0, 1] += 1
        elif classes[idx[0]] == 'dining_room':
            predicted_count[1, 1] += 1
        elif classes[idx[0]] == 'drawing_room':
            predicted_count[2, 1] += 1
        elif classes[idx[0]] == 'others':
            predicted_count[3, 1] += 1
        elif classes[idx[0]] == 'toilet_room':
            predicted_count[4, 1] += 1

        predicted_count[class_id, 2] += 1
        count+=1
    accuracy = 100*correct/float(count)
    print('Accuracy of {} class is {:2.2f}%'.format(class_name,accuracy))
    accuracies_list.append(accuracy)

wb.save(xlsx_path)

print('Average test accuracy is = {:2.2f}%'.format(sum(accuracies_list)/len(accuracies_list)))   # This is not weighted between number of samples

print(predicted_count)
precision = predicted_count[:, 0]/predicted_count[:, 2]
print(precision)
precision_avg = sum(predicted_count[:, 0])/sum(predicted_count[:, 2])
print(precision_avg)

recall = predicted_count[:, 0]/predicted_count[:, 1]
print(recall)
recall_avg = sum(predicted_count[:, 0]/predicted_count[:, 1] * predicted_count[:, 2]/sum(predicted_count[:, 2]))
print(recall_avg)

print("done")