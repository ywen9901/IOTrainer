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

![](https://github.com/yww1327/IOTrainer/blob/main/readme/cameraConfigSetup.png) |


## Dependencies
* Python 3
* OpenCV (3.4.1+ to use the function ```cv2.dnn.readNetFromTensorflow```)
* imutils (for video streaming)
* Flask (to build webpage)

## Implementation
#### 0. Set up all dependencies
I used the following command to install the package needed. You can choose to install them in base or in the virtual environmnet you created.
```
$ pip3 install imutils
$ pip3 install Flask
```
