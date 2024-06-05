import cv2
import numpy as np
from pyzbar.pyzbar import decode

video = cv2.VideoCapture('./videos/QRVideo2.mp4')

while True:
    ret, frame = video.read()
    if ret:
        resize_frame = cv2.resize(frame, (0, 0), None, 0.6, 0.6)

        for code in decode(resize_frame):
            print(code)
            myData = code.data.decode('utf-8')
            pts = np.array([code.polygon], np.int32)
            # print("pts", pts)
            reshape_pts = pts.reshape((-1, 1, 2))
            # print("reshape_pts", reshape_pts)
            cv2.polylines(resize_frame, [reshape_pts], True, (0, 0, 255), thickness=5)
            pts2 = code.rect
            cv2.putText(resize_frame, myData, (pts2[0], pts2[1]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

        cv2.imshow('frame', resize_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
