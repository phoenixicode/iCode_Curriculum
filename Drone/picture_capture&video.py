from djitellopy import tello
import cv2
import time

t=tello.Tello()
t.connect()

t.streamon()
frames=t.get_frame_read()

t.takeoff()
picname="firstpic"+time.ctime()+".png"
cv2.imwrite(picname, frames.frame)

t.land()


import time, cv2
from threading import Thread
from djitellopy import Tello

drone = tello.Tello()

drone.connect()

keepRecording = True
drone.streamon()
frame_read = drone.get_frame_read()

def videoRecorder():
    # create a VideoWrite object, recoring to ./video.avi
    height, width, _ = frame_read.frame.shape
    video_name="video "+time.ctime()+".avi"
    video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'XVID'), 30, (width, height))

    while keepRecording:
        video.write(frame_read.frame)
        time.sleep(1 / 30)

    video.release()


videoRecorder()





# from djitellopy import tello
# import cv2
# import time
#
# t = tello.Tello()
# t.connect()
#
# t.streamon()
# frames = t.get_frame_read()
#
# t.takeoff()
# cv2.imwrite("Picture.png",frames.frame)
#
# t.land()
