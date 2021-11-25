import os
from dotenv import load_dotenv
import RPi.GPIO as GPIO
import time

load_dotenv() 
# Setup listen event on GPIO
# Raspberry Pi GPIO pin that senses for HIGH signal
GPIO_PIN = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

ups = 0
while True:
    if GPIO.input(GPIO_PIN):
        ups+=1
    else:
        if ups > 0:
            ups -= 1
    if ups == 10:
        print('ACTIVATE')
        ups = 0
        time.sleep(10)

    print(ups)
    time.sleep(0.05)