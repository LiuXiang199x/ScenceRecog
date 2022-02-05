# 旋转 | 反射变换(Rotation/reflection): 随机旋转图像一定角度; 改变图像内容的朝向;
import cv2 as cv
import imutils
import argparse

origin_img_path = "./DEDUCE/data/val/bed_room/RGB100W_542500000083_116445085381751238.jpg"

# 逆时针以图像中心旋转45度
# - (cX,cY): 旋转的中心点坐标
# - 45: 旋转的度数，正度数表示逆时针旋转，而负度数表示顺时针旋转。
# - 1.0：旋转后图像的大小，1.0原图，2.0变成原来的2倍，0.5变成原来的0.5倍
# OpenCV不会自动为整个旋转图像分配空间，以适应帧。旋转完可能有部分丢失。
# 如果希望在旋转后使整个图像适合视图，则要进行优化，用imutils.rotate_bound.
# #

def normal_rotation():
    image = cv.imread(origin_img_path)
    cv.imshow("Original", image)

    # 获取图像的维度，并计算中心
    (h, w) = image.shape[:2]
    (cX, cY) = (w // 2, h // 2)

    M = cv.getRotationMatrix2D((cX, cY), 45, 2.0)

    rotated = cv.warpAffine(image, M, (w, h))
    cv.imshow("Rotated by 45 Degrees", rotated)
    cv.imwrite("./数据增强/pics/flips_rotation_transpose/normal_rotation.jpg", rotated)

    cv.waitKey(0)
    cv.destroyAllWindows()

def imutils_rotation():
    image = cv.imread(origin_img_path)
    cv.imshow("Original", image)

    rotated = imutils.rotate_bound(image, 5)
    cv.imwrite("./数据增强/pics/flips_rotation_transpose/imutils_rotation.jpg", rotated)

    cv.imshow("Rotated by XX Degrees", rotated)

    cv.waitKey(0)
    cv.destroyAllWindows()

imutils_rotation()
normal_rotation()