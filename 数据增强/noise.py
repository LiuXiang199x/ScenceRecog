# 噪声扰动(noise): 对图像的每个像素RGB进行随机扰动, 常用的噪声模式是椒盐噪声和高斯噪声;
import cv2 as cv
import imutils
import argparse

origin_img_path = "./DEDUCE/data/val/bed_room/RGB100W_542500000083_116445085381751238.jpg"


