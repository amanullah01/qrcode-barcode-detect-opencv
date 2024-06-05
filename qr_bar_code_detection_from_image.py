import cv2
import numpy as np
from pyzbar.pyzbar import decode

image = cv2.imread('./images/MultipleQR_Bar_code.PNG')

# decode qr bar code image
for code in decode(image):
    print(code.data.decode('utf-8'))

cv2.imshow('image', image)
cv2.waitKey(0)
