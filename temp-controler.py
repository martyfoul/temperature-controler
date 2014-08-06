import os
import glob
import time
import RPi.GPIO as io # load RPi.GPIO
io.setmode(io.BCM) # for io

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

power_pin = 20 # power to relay
temp_set = 70.0 # the target temperature

io.setup(power_pin, io.OUT) 
io.setup(power_pin, False)

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c #, temp_f
	
while True:
    if read_temp() < temp_set:
	    print("POWER ON")
	    io.output(power_pin, True)
	    print(read_temp())
	    time.sleep(3)

    else: print("POWER OFF")
    io.output(power_pin, False)
    print(read_temp())	
    time.sleep(3)
