# iot_final_project

## Hardware
* Raspberry pi 3 ([Set Up Manual](https://github.com/yww1327/iot_final_project/blob/main/setupManual.pdf)
* Pi Camera

## Dependencies
* Python 3
* OpenCV

## Implementation
0. Set up your raspi and picamera
1. Clone this repo to your raspi
2. Run terminal input ```$ python test.py```


## To Be Strengthened
### Slow operation speed
[Streaming: OpenCV v.s. PiCamera](https://blog.xuite.net/jblabs/blog/463506239-%5B%E8%BB%9F%E9%AB%94%5D+%E4%BD%BF%E7%94%A8+Raspberry+Pi+Camera+Module+%2B+Python+%2B+OpenCV+%E9%80%B2%E8%A1%8C%E5%8B%95%E6%85%8B%E8%87%89%E9%83%A8%E8%BE%A8%E8%AD%98)

僅進行streaming的時候延遲不嚴重，但是run過estimation function之後延遲大約會是2至3秒
目前是以降低```test_video.py```中```inWidth```和```inHeight```變數來降低延遲的嚴重程度，但降低的同時也會影響準確率，以目前所設定的180再下降就會有辨識錯誤的問題
推測如果以picamera本身start_preview或start_recording取代cv.imshow()，再以addLayout的方式在streaming video上疊上skeletons，可能可以加快畫面render的速度


### Network connection
[PiCamera Web Streaming](https://picamera.readthedocs.io/en/latest/recipes2.html#web-streaming)

[Video Streaming on Flask](https://www.hackster.io/ruchir1674/video-streaming-on-flask-server-using-rpi-ef3d75)

以Http server/Flask讓streaming畫面能夠顯示在網頁上，將host設定為本地，設定port後，在其他位於同LAN的devices上輸入網址```$(raspi_ip):port```，可以看到picamera streaming的影像
raspi ip查詢方法如下
在terminal輸入
```
$ ip addr
```
會得到如下圖的畫面

![](https://github.com/yww1327/iot_final_project/blob/main/README_pic/ip_addr.PNG)

"inet"後的數字字串就是raspi的ip，以此圖片為例，raspi ip為172.20.10.5


## Reference
https://github.com/quanhua92/human-pose-estimation-opencv/blob/master/openpose.py

https://nanonets.com/blog/human-pose-estimation-2d-guide/
