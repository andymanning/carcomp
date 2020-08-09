#!/usr/bin/env python
# Creates an HTTP server websocket communication.

import argparse
import base64
import cv2
import picamera
from PIL import Image
import cStringIO as io 
import tornado.web
import tornado.websocket
from tornado.ioloop import PeriodicCallback

class WebSocket(tornado.websocket.WebSocketHandler):
    
    # Allow calls from anywhere!! 
    # (this is safe for the car app as it's a closed system)
    def check_origin(self, origin):
        return True

    def on_message(self, message):
        parts = message.split(":")
        command = parts[0]
        global cameraName 
        cameraName = parts[1]

        # Start an infinite loop when this is called
        if command == "read_camera":
            print ("starting stream for %s camera" %(cameraName))
            self.camera_loop = PeriodicCallback(self.loop, 10)
            self.camera_loop.start()
        elif command == "stop_camera":
            print ("stopping stream from %s camera" %(cameraName))
            try:
                self.camera_loop.stop()
            except:
               pass #do nothing if loop can't be stoppedS
         
        else:
            print("Unsupported function: " + message)

    #Sends camera images in an infinite loop.  
    def loop(self):
        sio = io.StringIO()

        if cameraName == "front":
            _, frame = frontCamera.read()
            img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            img.save(sio, "JPEG")
        elif cameraName == "rear":
            _, frame = rearCamera.read()
            img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            img.save(sio, "JPEG")
        elif cameraName == "cabin":
           cabinCamera.capture(sio, "jpeg", use_video_port=True)
        else:
            print("ERROR: Camera %s is unknown" %(cameraName))

        try:
            self.write_message(base64.b64encode(sio.getvalue()))
        except tornado.websocket.WebSocketClosedError:
            self.camera_loop.stop()

parser = argparse.ArgumentParser(description="Starts a webserver that connects to a webcam.")
parser.add_argument("--port", type=int, default=8001, help="The port on which to serve the website.")
parser.add_argument("--front_id", type=int, default=1, help="USB Id of the front camera")
parser.add_argument("--rear_id", type=int, default=3, help="USB Id of the rear camera")
args = parser.parse_args()

#Gobal vars
cameraName = None

#resolutions = {"high": (1280, 720), "medium": (640, 480), "low": (320, 240)}

frontCamera = cv2.VideoCapture(args.front_id)
frontCamera.set(3,640)
frontCamera.set(4,480)

rearCamera = cv2.VideoCapture(args.rear_id)
rearCamera.set(3,640)
rearCamera.set(4,480)

cabinCamera = picamera.PiCamera()
cabinCamera.resolution = (640,480)

handlers = [(r"/websocket", WebSocket)]

application = tornado.web.Application(handlers)
application.listen(args.port)
tornado.ioloop.IOLoop.instance().start()
