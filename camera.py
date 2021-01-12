import cv2 as cv
import matplotlib.pyplot as plt
from imutils.video.pivideostream import PiVideoStream
import imutils
import time
import numpy as np


net = cv.dnn.readNetFromTensorflow("graph_opt.pb")
inWidth = 180
inHeight = 180
thr = 0.2

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


def pose_estimation_shoulder_press(frame):
    frameWidth = frame.shape[1]
    frameHeight = frame.shape[0]
    net.setInput(cv.dnn.blobFromImage(frame, 1.0, (inWidth, inHeight),
                                      (127.5, 127.5, 127.5), swapRB=True, crop=False))

    out = net.forward()
    out = out[:, :19, :, :]

    assert(len(BODY_PARTS) == out.shape[1])

    points = []
    for i in range(len(BODY_PARTS)):
        heatMap = out[0, i, :, :]

        _, conf, _, point = cv.minMaxLoc(heatMap)
        x = (frameWidth * point[0]) / out.shape[3]
        y = (frameHeight * point[1]) / out.shape[2]
        points.append((int(x), int(y)) if conf > thr else None)

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
                       0, 0, 360, (0, 255, 255), cv.FILLED)
            cv.ellipse(frame, points[idTo], (3, 3), 0,
                       0, 360, (0, 255, 255), cv.FILLED)

    t, _ = net.getPerfProfile()
    freq = cv.getTickFrequency() / 1000

    if points[3] and points[6]:
        distance = points[3][1]-points[6][1]
        if abs(distance) > 50:
            cv.putText(frame, "Error", (10, 80),
                       cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            if points[3][1] > points[6][1]:
                cv.ellipse(frame, (points[6][0], points[3][1]), (5, 5),
                           0, 0, 360, (0, 0, 255), cv.FILLED)
            else:
                cv.ellipse(frame, (points[3][0], points[6][1]), (5, 5),
                           0, 0, 360, (0, 0, 255), cv.FILLED)

    return frame


def pose_estimation_chest_press(frame):
    frameWidth = frame.shape[1]
    frameHeight = frame.shape[0]
    net.setInput(cv.dnn.blobFromImage(frame, 1.0, (inWidth, inHeight),
                                      (127.5, 127.5, 127.5), swapRB=True, crop=False))

    out = net.forward()
    out = out[:, :19, :, :]

    assert(len(BODY_PARTS) == out.shape[1])

    points = []
    for i in range(len(BODY_PARTS)):
        heatMap = out[0, i, :, :]

        _, conf, _, point = cv.minMaxLoc(heatMap)
        x = (frameWidth * point[0]) / out.shape[3]
        y = (frameHeight * point[1]) / out.shape[2]
        points.append((int(x), int(y)) if conf > thr else None)

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
                       0, 0, 360, (0, 255, 255), cv.FILLED)
            cv.ellipse(frame, points[idTo], (3, 3), 0,
                       0, 360, (0, 255, 255), cv.FILLED)

    t, _ = net.getPerfProfile()
    freq = cv.getTickFrequency() / 1000

    if points[3] and points[6]:
        distance = points[3][1]-points[6][1]
        if abs(distance) > 50:
            cv.putText(frame, "Error", (10, 80),
                       cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            if points[3][1] > points[6][1]:
                cv.ellipse(frame, (points[6][0], points[3][1]), (5, 5),
                           0, 0, 360, (0, 0, 255), cv.FILLED)
            else:
                cv.ellipse(frame, (points[3][0], points[6][1]), (5, 5),
                           0, 0, 360, (0, 0, 255), cv.FILLED)

    return frame


def pose_estimation_plank(frame):
    frameWidth = frame.shape[1]
    frameHeight = frame.shape[0]
    net.setInput(cv.dnn.blobFromImage(frame, 1.0, (inWidth, inHeight),
                                      (127.5, 127.5, 127.5), swapRB=True, crop=False))

    out = net.forward()
    out = out[:, :19, :, :]

    assert(len(BODY_PARTS) == out.shape[1])

    points = []
    for i in range(len(BODY_PARTS)):
        heatMap = out[0, i, :, :]

        _, conf, _, point = cv.minMaxLoc(heatMap)
        x = (frameWidth * point[0]) / out.shape[3]
        y = (frameHeight * point[1]) / out.shape[2]
        points.append((int(x), int(y)) if conf > thr else None)

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
                       0, 0, 360, (0, 255, 255), cv.FILLED)
            cv.ellipse(frame, points[idTo], (3, 3), 0,
                       0, 360, (0, 255, 255), cv.FILLED)

    t, _ = net.getPerfProfile()
    freq = cv.getTickFrequency() / 1000

    if points[2] and points[8]:
        distance = points[2][1]-points[8][1]
        if abs(distance) > 50:
            cv.putText(frame, "Error", (10, 80),
                       cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            if points[2][1] > points[8][1]:
                cv.ellipse(frame, (points[8][0], points[2][1]), (5, 5),
                           0, 0, 360, (0, 0, 255), cv.FILLED)
            else:
                cv.ellipse(frame, (points[2][0], points[8][1]), (5, 5),
                           0, 0, 360, (0, 0, 255), cv.FILLED)
    elif points[5] and points[11]:
        distance = points[5][1]-points[11][1]
        if abs(distance) > 50:
            cv.putText(frame, "Error", (10, 80),
                       cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            if points[5][1] > points[11][1]:
                cv.ellipse(frame, (points[11][0], points[5][1]), (5, 5),
                           0, 0, 360, (0, 0, 255), cv.FILLED)
            else:
                cv.ellipse(frame, (points[5][0], points[11][1]), (5, 5),
                           0, 0, 360, (0, 0, 255), cv.FILLED)

    return frame


class VideoCamera(object):
    vs = PiVideoStream().start()

    def __init__(self, flip=False):
        self.flip = flip
        time.sleep(2.0)

    def __del__(self):
        vs.stop()

    def flip_if_needed(self, frame):
        if self.flip:
            return np.flip(frame, 0)
        return frame

    def get_frame_shoulder_press(self):
        frame = self.flip_if_needed(self.vs.read())
        frame = pose_estimation_shoulder_press(frame)
        ret, jpeg = cv.imencode('.jpg', frame)
        return jpeg.tobytes()

    def get_frame_chest_press(self):
        frame = self.flip_if_needed(self.vs.read())
        frame = pose_estimation_chest_press(frame)
        ret, jpeg = cv.imencode('.jpg', frame)
        return jpeg.tobytes()

    def get_frame_plank(self):
        frame = self.flip_if_needed(self.vs.read())
        frame = pose_estimation_plank(frame)
        ret, jpeg = cv.imencode('.jpg', frame)
        return jpeg.tobytes()
