#Stop anything that may have been running before
killall python
killall python3

#Start up the camera server
./camera-server/camera-server.py& 

#Start up the web server
python3 -m http.server 8000&
