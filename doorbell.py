from googlehomepush import GoogleHome
import time 
import os
from dotenv import load_dotenv
from threading import Thread
import RPi.GPIO as GPIO
import sys

load_dotenv() 

HOSTS = os.getenv('HOSTS', '').split(',')
SOUND_URL = os.getenv('SOUND_URL', "https://www.myinstants.com/media/sounds/roblox-death-sound_1.mp3")

print('starting service')
print(HOSTS)


def playSound(host):
    try:
        googleDevice = GoogleHome(host=host)
        googleDevice.play(SOUND_URL)
    except:
        pass

def playSounds():
    for host in HOSTS:
        thread = Thread(target = playSound, args=[host])
        thread.start()


GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# Here we just wire the  GPIO inputs to their respective callback functions
GPIO.add_event_detect(17, GPIO.RISING, callback=playSounds, bouncetime=500)

while True:
    time.sleep(10)