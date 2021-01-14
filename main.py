from flask import Flask, render_template, Response, request
# import from camera.py
from camera import VideoCamera
import time
import threading
import os
import cv2 as cv
from imutils.video.pivideostream import PiVideoStream
import imutils

pi_camera = VideoCamera(flip=False)


app = Flask(__name__)


# Route for index and render PiCamera streaming
@app.route('/')
def index():
    return render_template('index.html')


def gen_shoulder_press(camera):
    while True:
        frame = camera.get_frame_shoulder_press()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


def gen_chest_press(camera):
    while True:
        frame = camera.get_frame_chest_press()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


def gen_plank(camera):
    while True:
        frame = camera.get_frame_plank()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/shoulder_press')
def shoulder_press():
    return Response(gen_shoulder_press(pi_camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/chest_press')
def chest_press():
    return Response(gen_chest_press(pi_camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/plank')
def plank():
    return Response(gen_plank(pi_camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':

    app.run(host='0.0.0.0', debug=False)
