import time

from nanoleafapi.nanoleaf import GREEN, WHITE
from pykinect2 import PyKinectRuntime, PyKinectV2
import numpy as np
import cv2
import lights

#declaration of the depth camera object
kinectDepth = PyKinectRuntime.PyKinectRuntime(PyKinectV2.FrameSourceTypes_Depth)

#image resolution declaraion
x = 424
y = 512

#initializing the nanoleaf wall
# lights.allOn(GREEN)
# lights.allSetBright(100)


while True:
    #depth frame is a one dimentional array that contains corodinate data of each pixel
    depthFrame = kinectDepth.get_last_depth_frame()
    #depth data will be scaled to match the max distance that the kinect can read which is about 2600 mm
    #displaying the scaled depth data at the middle pixel in the array
    scaledDepth = depthFrame[int(x*0.5 + (y*0.5)*512)]/26
    print(scaledDepth)
    #converting the depth data to 8 bit unsigned integer to be rendered by the opencv package and return image data
    depthFrame = depthFrame.astype(np.uint8)
    depthFrame = np.reshape(depthFrame,(x, y))
    depthFrame = cv2.cvtColor(depthFrame, cv2.COLOR_GRAY2BGR)

    #note: this should be commented out, as well as any code that will be used to process images, if using with the raspberry pi in zetta, to reduce processing load, 
    cv2.imshow("depthFrame",depthFrame)
    cv2.waitKey(1)







