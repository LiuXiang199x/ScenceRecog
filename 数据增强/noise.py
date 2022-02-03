# 噪声扰动(noise): 对图像的每个像素RGB进行随机扰动, 常用的噪声模式是椒盐噪声和高斯噪声;
import cv2 as cv
import imutils
import argparse
import numpy as np
import random

origin_img_path = "./数据增强/pics/original/RGB100W_542500000083_116445085381751238.jpg"


def sp_noise(image, prob):
    '''
    添加椒盐噪声
    prob:噪声比例 
    '''
    output = np.zeros(image.shape,np.uint8)
    thres = 1 - prob 
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output
 
def gasuss_noise(image, mean=0, var=0.005):
    ''' 
    添加高斯噪声
    mean : 均值 
    var : 方差
    '''
    image = np.array(image/255, dtype=float)
    noise = np.random.normal(mean, var ** 0.5, image.shape)
    out = image + noise
    if out.min() < 0:
        low_clip = -1.
    else:
        low_clip = 0.
    out = np.clip(out, low_clip, 1.0)
    out = np.uint8(out*255)
    #cv.imshow("gasuss", out)
    return out

img = cv.imread(origin_img_path)
spicedSalt_img = sp_noise(img, 0.02)

gauss_img = gasuss_noise(img)
cv.imwrite("./数据增强/pics/noise/gauss_mean0_var0.005.jpg", gauss_img)
cv.imwrite("./数据增强/pics/noise/spicedSalt_prob0.02.jpg", spicedSalt_img)

cv.imshow("111111:", spicedSalt_img)
cv.waitKey(0)
print(spicedSalt_img.shape)