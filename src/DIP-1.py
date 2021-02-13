#OpenCV Python 灰度和色彩图片的均衡化直方图
# https://makeronsite.com/opencv-python-equalizing-image-histograms.html


import cv2
import numpy as np
import matplotlib.pyplot as plt


# 以灰度模式读取图片
img_gray = cv2.imread('TFC.jpg',0)
# 显示原始图片
plt.imshow(img_gray,cmap='gray')
plt.show()

# 使用 `cv2.equalizeHist` 函数进行归一化图像亮度和增强图像对比度
img_equHist_gray = cv2.equalizeHist(img_gray)
plt.imshow(img_equHist_gray,cmap='gray')
plt.show()

#cv2.waitKey(0)
#cv2.destroyAllWindows()