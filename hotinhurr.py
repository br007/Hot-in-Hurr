import os
import glob
import time
import RPi.GPIO as GPIO
import pygame
#initialize the device 
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'


def initLights():
#initialize lights
    GPIO.setmode(GPIO.BCM)
    GPIO.cleanup()
    GPIO.setwarnings(False)
    GPIO.setup(17,GPIO.OUT)
    GPIO.setup(21,GPIO.OUT)


def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines


initLights()
hold=0
splay=0

while True:
    lines = read_temp_raw()

    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()

    equals_pos = lines[1].find('t=')

    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        all_temp = "Celsius: " + str(temp_c) + " Farenheit: " + str(temp_f)


    if temp_f >79.6:
        if splay == 0:
            pygame.mixer.quit()
            pygame.mixer.init()
            pygame.mixer.music.load("hot.mp3")
            pygame.mixer.music.play()
            splay=1

    if hold==0:
        print "No Comparison"
    else:
        if far_hold < temp_f:
            GPIO.output(17,GPIO.HIGH)
            GPIO.output(21,GPIO.LOW)
    #print far_hold
        elif far_hold> temp_f:
            GPIO.output(17,GPIO.LOW)
            GPIO.output(21,GPIO.HIGH)
            #print far_hold
        else:
            GPIO.output(17,GPIO.LOW)
            GPIO.output(21,GPIO.LOW)
        #print far_hold

    hold=1
    far_hold=temp_f

    print all_temp
    time.sleep(1)
