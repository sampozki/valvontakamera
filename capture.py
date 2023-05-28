import cv2
import time

cap = cv2.VideoCapture('rtsp://10.8.8.136:554') # it can be rtsp or http stream

ret, frame = cap.read()

if cap.isOpened():
    _,frame = cap.read()
    cap.release() #releasing camera immediately after capturing picture
    if _ and frame is not None:
        cv2.imwrite('latest.jpg', frame)
        cv2.imwrite('images/{}.jpg'.format(str(time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()))), frame)


