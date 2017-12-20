from scipy import misc
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage
# (1) 载入Lena图像，并使用灰度颜色表将其在子图中显示出来。
image = misc.lena().astype(np.float32)
plt.subplot(221)
plt.title("Original Image")
img = plt.imshow(image, cmap=plt.cm.gray)
plt.axis("off")
# 2) 中值滤波器扫描信号的每一个数据点，并替换为相邻数据点的中值。
plt.subplot(222)
plt.title("Median Filter")
filtered = ndimage.median_filter(image, size=(42,42))
plt.imshow(filtered, cmap=plt.cm.gray)
plt.axis("off" )
# (3) 旋转图像并显示在第三个子图中。
plt.subplot(223)
plt.title("Rotated")
rotated = ndimage.rotate(image, 90)
plt.imshow(rotated, cmap=plt.cm.gray)
plt.axis("off")
# (4) Prewitt滤波器是基于图像强度的梯度计算。对图像应用Prewitt滤波器并显示在第四个子图中
plt.subplot(224)
plt.title("Prewitt Filter")
filtered = ndimage.prewitt(image)
plt.imshow(filtered, cmap=plt.cm.gray)
plt.axis("off")
plt.show()