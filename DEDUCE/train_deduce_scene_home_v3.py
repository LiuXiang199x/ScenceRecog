import argparse
import torch
from torch.autograd import Variable as V
import torchvision.models as models
from torchvision import transforms as trn
from torch.nn import functional as F
import os
from PIL import Image
from config import places_dir,sun_dir,vpc_dir

parser = argparse.ArgumentParser(description='DEDUCE Scene_Only Evaluation')
parser.add_argument('--dataset',default='places',help='dataset to test')
parser.add_argument('--hometype',default='home1',help='home type to test')
parser.add_argument('--floortype',default='data_0',help='data type to test')
parser.add_argument('--envtype',default='home',help='home or office type environment')

global args
args = parser.parse_args()

# th architecture to use
arch = 'resnet18'

# load the pre-trained weights
model_file = 'models/{}_best_{}.pth.tar'.format(arch,args.envtype)


checkpoint = torch.load(model_file, map_location=lambda storage, loc: storage)
state_dict = {str.replace(k,'module.',''): v for k,v in checkpoint['state_dict'].items()}

model = models.__dict__[arch](num_classes=7)
model.load_state_dict(state_dict)


model2 = models.__dict__[arch](num_classes=5)
model2_dict = model2.state_dict()

del state_dict['fc.weight']
del state_dict['fc.bias']
model2_dict.update(state_dict)
model2.load_sate_dict(model2_dict)
print("done")
