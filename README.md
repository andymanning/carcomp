# carcomp
Go and Webix based Car Computer for a Raspberry Pi

##Raspberry Pi Setup Links
https://desertbot.io/blog/headless-raspberry-pi-4-ssh-wifi-setup
https://desertbot.io/blog/raspberry-pi-touchscreen-kiosk-setup


#Power on via push switch
Enabled by default, uses pin 5

#Power off via push switch
Add the line "dtoverlay=gpio-shutdown" to "/boot/config.txt"
Push button on pin 5 and it will shutdown


#Turn on a LED when pi starts
Add the line "gpio=15=op,dh" to "/boot/config.txt"
* change 15 to be whatever you want!

#Link for powerup/powerdown
https://www.embedded-computing.com/guest-blogs/raspberry-pi-power-up-and-shutdown-with-a-physical-button

