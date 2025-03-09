import cv2
import numpy as np
from djitellopy import tello
import time

dr = tello.Tello()
dr.connect()
print(dr.get_battery())
dr.streamon()
dr.takeoff()

dr.move_up(70)
dr.sent_rc_control(0, 0, 10, 0)
time.sleep(2.2)

w, h = 720, 600

fbrange = [7200, 7800]
pid = [0.4, 0.4, 0]
perror = 0


def findface(img):
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(img_grey, 1.2, 8)

    myFaceListC = []
    myFaceListArea = []

    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cx = x + w // 2
        cy = y + h // 2
        area = w * h
        cv2.circle(img, (cx, cy), 5, (0, 255, 0), cv2.FILLED)
        myFaceListC.append([cx, cy])
        myFaceListArea.append(area)

    if len(myFaceListArea) != 0:
        i = myFaceListArea.index(max(myFaceListArea))
        return img, [myFaceListC[i],myFaceListArea[i]]
    else:
        return img, [[0, 0], 0]

