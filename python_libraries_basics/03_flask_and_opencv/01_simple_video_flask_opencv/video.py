import cv2
# import numpy as np -> for later
# import datetime -> for later 

class Video_Object():
    def __init__(self):
        self.video = cv2.VideoCapture("Pexels Videos 2609.mp4")
       
    def __del__(self):
        #releasing camera
        self.video.release()

    def get_frame(self):
        #extracting frames
        success, video = self.video.read() # self.video.read() -> self.video is the name created by the class constructor

        # encode OpenCV raw frame to jpg and displaying it
        ret, jpeg = cv2.imencode('.jpg', video)
        return jpeg.tobytes()