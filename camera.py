from time import time
import cv2
from imutils.video import VideoStream
import imutils
import time

class Camera(object):
    """An emulated camera implementation that streams a repeated sequence of
    files 1.jpg, 2.jpg and 3.jpg at a rate of one frame per second."""

    def __init__(self):
    	self.vs = VideoStream(src=0).start()
    	time.sleep(2.0)		 

    def get_frame(self):
    	frame = self.vs.read()
    	frame = imutils.resize(frame, width=800)
    	ret, jpeg = cv2.imencode('.jpg', frame)
    	return jpeg.tobytes()

if __name__ == '__main__':
	camera = Camera()
	with open('test.jpg','wb') as picture :
		text = camera.get_frame()
		picture.write(text)