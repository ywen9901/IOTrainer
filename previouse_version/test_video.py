from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

# grapsh_opt.pb = model weight
net = cv.dnn.readNetFromTensorflow("graph_opt.pb")
inWidth = 180
inHeight = 180
thr = 0.2

# list body parts
BODY_PARTS = {"Nose": 0, "Neck": 1, "RShoulder": 2, "RElbow": 3, "RWrist": 4,
              "LShoulder": 5, "LElbow": 6, "LWrist": 7, "RHip": 8, "RKnee": 9,
              "RAnkle": 10, "LHip": 11, "LKnee": 12, "LAnkle": 13, "REye": 14,
              "LEye": 15, "REar": 16, "LEar": 17, "Background": 18}

POSE_PAIRS = [["Neck", "RShoulder"], ["Neck", "LShoulder"], ["RShoulder", "RElbow"],
              ["RElbow", "RWrist"], ["LShoulder", "LElbow"], ["LElbow", "LWrist"],
              ["Neck", "RHip"], ["RHip", "RKnee"], [
    "RKnee", "RAnkle"], ["Neck", "LHip"],
    ["LHip", "LKnee"], ["LKnee", "LAnkle"], [
    "Neck", "Nose"], ["Nose", "REye"],
    ["REye", "REar"], ["Nose", "LEye"], ["LEye", "LEar"]]


#estimation function
def pose_estimation(frame):
    frameWidth = frame.shape[1]
    frameHeight = frame.shape[0]
    net.setInput(cv.dnn.blobFromImage(frame, 1.0, (inWidth, inHeight),
                                      (127.5, 127.5, 127.5), swapRB=True, crop=False))

    out = net.forward()
    # MobileNet output [1, 57, -1, -1], we only need the first 19 elements
    out = out[:, :19, :, :]

    assert(len(BODY_PARTS) == out.shape[1])

    points = []
    # add every points into points[]
    for i in range(len(BODY_PARTS)):
        heatMap = out[0, i, :, :]

        _, conf, _, point = cv.minMaxLoc(heatMap)
        x = (frameWidth * point[0]) / out.shape[3]
        y = (frameHeight * point[1]) / out.shape[2]
        points.append((int(x), int(y)) if conf > thr else None)
  
    # pair the body parts
    for pair in POSE_PAIRS:
        partFrom = pair[0]
        partTo = pair[1]
        assert(partFrom in BODY_PARTS)
        assert(partTo in BODY_PARTS)

        idFrom = BODY_PARTS[partFrom]
        idTo = BODY_PARTS[partTo]

        if points[idFrom] and points[idTo]:
            cv.line(frame, points[idFrom], points[idTo], (0, 255, 0), 3)
            cv.ellipse(frame, points[idFrom], (3, 3),
                       0, 0, 360, (0, 0, 255), cv.FILLED)
            cv.ellipse(frame, points[idTo], (3, 3), 0,
                       0, 360, (0, 0, 255), cv.FILLED)

    t, _ = net.getPerfProfile()
    freq = cv.getTickFrequency() / 1000
    
    # compare left and right elbow to estimate the accuracy of the pose of shoulder press
    if points[3] and points[6]:
        distance = points[3][1]-points[6][1]
        if abs(distance) > 50:
            # show "Error" on monitor when detecting wrong pose
            cv.putText(frame, "Error", (10, 80), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        
    cv.putText(frame, '%.2fms' % (t / freq), (10, 20),
               cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))

    return frame

# set up picamera
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))

time.sleep(0.1)

# operation for every frame in streaming video
# the function below is actually keep taking photos and put into array while streaming
# by delete the front element, which means the shown frame, the monitor can show the following frame by continuously getting the front element of the array
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):  
    image = frame.array
    
    estimated_image = pose_estimation(image)
    image = estimated_image
    
    # create a window to show the processed frames
    cv.imshow("Monitor", image)
    key = cv.waitKey(1) & 0xFF
    
    rawCapture.truncate(0)
    
    # press q to exit this program
    if key == ord("q"):
        break
