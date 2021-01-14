# IOTrainer
IOTrainer is an application working on edge devices, such as Raspberry Pi, to check poses during your workout process. It contains the functions of drawing body skeletons and showing the right position point of the workout poses. With PiCamera, IOTrainer could capture and stream in the browser. Other devices can browse the webpage by connecting on same LAN. (The method will be mentioned [below]().)

## Demo
| Show Skeletons When Human Body Detected | Show Error and Right Pose Point |
| ---- | ---- |
| ![](https://github.com/yww1327/IOTrainer/blob/main/readme/skeletons.png) | ![](https://github.com/yww1327/IOTrainer/blob/main/readme/error.png) |

Check video demo [here]()!

## Hardware Required
* Raspberry Pi 3 (Check the setup manual [here](https://github.com/yww1327/IOTrainer/blob/main/readme/setupManual.pdf))
* Pi Camera
* 5V Transformer

| Needed Components | Configuration of the components |
| ---- | ---- |
| ![](https://github.com/yww1327/IOTrainer/blob/main/readme/neededHardware.jpg) | ![](https://github.com/yww1327/IOTrainer/blob/main/readme/hardwardConfig.jpg) | 

**NOTE**: Remember to enable camera configuration!!
 
![](https://github.com/yww1327/IOTrainer/blob/main/readme/cameraConfigSetup.png)

## Dependencies
* Python 3
* OpenCV (3.4.1+ to use the function ```cv2.dnn.readNetFromTensorflow```)
* imutils (for video streaming)
* Flask (to build webpage)

## Deployment
(**NOTE**: The delay in streaming could be severe due to the operation of OpenCV. The possible solutions will be listed [below]().)


### 0. Set up all dependencies

After installing Python and OpenCV, the installation of the following package is needed. You can choose to install in base or your own virtual environment.
```
$ pip3 install imutils
$ pip3 install Flask
```

### 1. Clone this repo

Open your Terminal and go to the path where you would like to store the files.
```
pi@raspberrypi:~ $ git clone https://github.com/yww1327/IOTrainer.git
``` 
### 2. Run main.py

Run ```main.py``` to start web server so that the captured and computed streaming video would shown in the browser.
```
pi@raspberrypi:~ $ cd IOTrainer
pi@raspberrypi:~/IOTrainer $python3 main.py
```

### 3. Browse the webpage

Enter address ```0.0.0.0:5000``` in the browser. You can see the streaming video captured by PiCamera.

### 4. Browse the webpage on other devices

Find your Pi ip address first by entering the following command in terminal.
```
$ ip addr
```
Then you can see the response like the picture shown below:

![](https://github.com/yww1327/IOTrainer/blob/main/readme/ip_addr.PNG)

The number string after "inet" is your Pi ip address. In this case, the Pi ip address is ```172.20.10.5```.
Connect other devices in the same LAN that Pi is in and enter ```172.20.10.5:5000``` in address bar of your browser.

## OpenCV Installation Record
Reference: [[raspberry pi] 編譯OpenCV_contrib](https://nancyyluu.blogspot.com/2017/12/raspberry-pi-opencvcontrib.html?fbclid=IwAR04es5w9Q44z1S-1ftq1_eWM-9EyT41oP0b8DH991P_87MF0ddEbGxG9PY)

I first installed OpenCV by pip.
```
$ sudo pip3 install opencv-python
```
However, when I run my project with it, there is a severe delay in streaming


## Reference
### About Pose Estimation

* [Machine learning for everyone: How to implement pose estimation in a browser using your webcam](https://thenextweb.com/syndication/2020/02/01/machine-learning-for-everyone-how-to-implement-pose-estimation-in-a-browser-using-your-webcam/)

* [Pose Estimation with TensorFlow 2.0](https://medium.com/@gsethi2409/pose-estimation-with-tensorflow-2-0-a51162c095ba)

* [Real Time Human Pose Estimation on the edge with Movidius NCS and OpenVINO](https://medium.com/@oviyum/real-time-human-pose-estimation-on-the-edge-with-movidius-ncs-and-openvino-ac3b13536)

* [HIIT PI](https://github.com/jingw222/hiitpi)

### About OpenCV

* [Deep Learning based Human Pose Estimation using OpenCV ( C++ / Python )](https://www.learnopencv.com/deep-learning-based-human-pose-estimation-using-opencv-cpp-python/)

### About Streaming on Raspberry pi

* [PiCamera Doucument -Web Streaming](https://picamera.readthedocs.io/en/latest/recipes2.html#web-streaming)

* [Video Streaming On Flask Server Using RPi](https://www.hackster.io/ruchir1674/video-streaming-on-flask-server-using-rpi-ef3d75)
