import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar

image = cv2.imread("add_your_image_here")

decodedObjects = pyzbar.decode(image)
for obj in decodedObjects:
    # print("Type: QRCODE")
    # print("Data:  b'www.copyassignment.com'")
    print("Type:", obj.type)
    print("Data: ", obj.data, "\n")


cv2.imshow("Frame", image)
cv2.waitKey(0)