# load the class label
file_name = '/media/agent/eb0d0016-e15f-4a25-8c28-0ad31789f3cb/Scene/DEDUCE/scene_30_all.txt'

classes = list()
with open(file_name) as class_file:
    for line in class_file:
        cur_sn = line.split()[0].rsplit('/')[-1].strip().rsplit('_')[0]+'_'+line.split()[0].rsplit('/')[-1].strip().rsplit('_')[1]
        if not cur_sn in classes:
            classes.append(cur_sn)
classes = tuple(classes)

file = '/media/agent/eb0d0016-e15f-4a25-8c28-0ad31789f3cb/Scene/DEDUCE/download_classes.txt'

classes_2 = list()
with open(file) as class_file:
    for line in class_file:
        cur_sn = line.split()[0]
        classes_2.append(cur_sn)
classes_2 = tuple(classes_2)

c = classes_2==classes

img_name = line.split()[0].rsplit('/')[-1].strip()
sn_name = line.split()[0].rsplit('/')[-1].strip().rsplit('_')[0]+'_'+line.split()[0].rsplit('/')[-1].strip().rsplit('_')[1]
print(img_name)