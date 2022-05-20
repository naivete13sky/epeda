import cv2
import numpy as np
file1 = 'before1.jpg'
file2 = 'after.jpg'

img1=cv2.imread(file1)
img2=cv2.imread(file2)

if img1.shape == img2.shape:
    print("shape一样")
else:
    print("shape not equal")

difference=cv2.subtract(img1,img2)
print(difference)
result=not np.any(difference)

if result is True:
    print("两张图一样")
else:
    cv2.imwrite("result.jpg",difference)
    print("两张图不一样")