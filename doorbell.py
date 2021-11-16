from googlehomepush import GoogleHome
import time 
import os
from dotenv import load_dotenv
from threading import Thread
import RPi.GPIO as GPIO
import sys

load_dotenv() 

HOSTS = os.getenv('HOSTS', '192.168.8.220').split(',')
SOUND_URL = os.getenv('SOUND_URL', "https://www.myinstants.com/media/sounds/movie_1.mp3")
GPIO_PIN = os.getenv('GPIO_PIN', 15)

print('starting service')
print(HOSTS)


def playSound(host):
    print('DONG')
    try:
        googleDevice = GoogleHome(host=host)
        googleDevice.play(SOUND_URL)
    except:
        pass

def playSounds():
    print('DING')
    for host in HOSTS:
        thread = Thread(target = playSound, args=[host])
        thread.start()

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# Here we just wire the  GPIO inputs to their respective callback functions
GPIO.add_event_detect(17, GPIO.RISING, callback=playSounds, bouncetime=500)

while True:
    time.sleep(10)