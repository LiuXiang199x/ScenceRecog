# 翻转变换(flip): 沿着水平或者垂直方向翻转图像;

import cv2 as cv
origin_img_path = "./DEDUCE/data/val/bed_room/RGB100W_542500000083_116445085381751238.jpg"


img = cv.imread(origin_img_path)
cv.imshow("123", img)
out = cv.waitKey(0)

h_img = cv.flip(img, 1)
# cv.imshow("123", h_img)
# out = cv.waitKey(0)

print(img.shape)   # （360，640，3）
dst = cv.resize(img, (200,800))

# cv.imshow("123", dst)
# out = cv.waitKey(0)

img_transpose = cv.transpose(img)
cv.imshow("123", img_transpose)
print(img_transpose.shape)   # （360，640，3）
out = cv.waitKey(0)
