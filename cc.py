import cv2,os
import numpy as np
img_standard = cv2.imread(os.path.join(os.getcwd(),r'test_dir\data\test_gui_main\person.jpg'))
img_current = cv2.imread(os.path.join(os.getcwd(),r'temp\person.jpg'))

if img_standard.shape == img_current.shape:
    print("shape一样")
else:
    print("shape not equal")

difference = cv2.subtract(img_standard, img_current)
print(difference)
result = not np.any(difference)

if result is True:
    print("两张图一样")
else:
    cv2.imwrite(r"temp\result.jpg", difference)
    print("两张图不一样")
