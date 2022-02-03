# 翻转变换(flip): 沿着水平或者垂直方向翻转图像;

import cv2 as cv
origin_img_path = "./DEDUCE/data/val/bed_room/RGB100W_542500000083_116445085381751238.jpg"


img = cv.imread(origin_img_path)
h_img = cv.flip(img, 1)
img_transpose = cv.transpose(img)

cv.imwrite("./数据增强/pics/flips_rotation_transpose/flips.jpg", h_img)
cv.imwrite("./数据增强/pics/flips_rotation_transpose/transpose.jpg", img_transpose)

cv.imshow("123", img)
cv.imshow("flips", h_img)
cv.imshow("transpose", img_transpose)
print(img_transpose.shape)   # （360，640，3）
out = cv.waitKey(0)
