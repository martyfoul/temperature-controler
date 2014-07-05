This code is for contolling the temperature of a kettle with a raspberry pi a themometer and a relay

Before running thermometer.py
	$ sudo modprobe w1-gpio
	$ sudo modprobe w1-therm
	$ cd /sys/bus/w1/devices
	$ ls
	$ cd 28-xxx (whatever shows up)
	$ cat w1_slave
