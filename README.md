# IOTrainer
IOTrainer is an application working on edge devices, such as Raspberry Pi, to check poses during your workout process. It contains the functions of drawing body skeletons and showing the right position point of the workout poses. With PiCamera, IOTrainer could capture and stream in the browser. Other devices can browse the webpage by connecting on same LAN. (The method will be mentioned [below]().)

## Demo
| Show Skeletons When Human Body Detected | Show Error and Right Pose Point |
| ---- | ---- |
| ![](https://github.com/yww1327/IOTrainer/blob/main/readme/skeletons.png) | ![](https://github.com/yww1327/IOTrainer/blob/main/readme/error.png) |

Check video demo [here]()! (**NOTE**: The delay in streaming could be severe due to the operation of OpenCV. The possible solutions will be listed [below]().)

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

## Implementation
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

