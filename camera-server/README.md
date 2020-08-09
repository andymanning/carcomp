

Camera Server
=============

What it does
============
Serves cameras connected to a raspberry pi via a websocket.
Can be used with the official raspberry pi camera and any number of USB cameras.

Acknowlegements
===============
I want to acknowledge the CAMP project by Patrick Fuller as it was his project that I used as the basis to create this server. If you are looking for a webserver and front end to serve webcams please see his project here: https://github.com/patrickfuller/camp. Many thanks Patrick!

Why I wrote it
==============
I needed a server that was capable of serving 3 cameras for a car computer project I'm building. The cameras are 
A USB camera looking in front of the car
A USB camera looking to the rear of the car
The Raspberry pi camera looking into the cabin of the car (I plan to use it for facial reconition!)

Installation
============

The server uses [tornado](http://www.tornadoweb.org/en/stable/) to create a web server that exposes a websocket. 
It can interact with the [Pi camera](http://www.adafruit.com/products/1367) with the aptly named [picamera](http://picamera.readthedocs.org/en/release-1.7/) module, or it can use USB webcams with [opencv](http://opencv.org/) and [Pillow](http://pillow.readthedocs.org/en/latest/installation.html). 

The command below installs both sets of dependencies.

```
sudo apt-get install python-dev python-pip python-opencv libjpeg-dev
sudo pip install tornado Pillow picamera
```

Once the dependencies are installed on your pi run the server.

```
python server.py
```

You then need to request images from the server via the websocket and display them in an img object. The wider project shows to utilise the server.

Options
=======
```
--port [number] - runs the server on a different port than 8000
--front_id [number] - the id of the front usb cameras (default 1)
--rear_id [number] - the id of the rear usb cameras (default 3)
```
The USB id of the cameras can be found by running 
```
> v4l2-ctl --list-devices
```