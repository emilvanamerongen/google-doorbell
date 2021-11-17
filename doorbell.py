from googlehomepush import GoogleHome
from pushnotifier import PushNotifier as pn
import time 
import os
from dotenv import load_dotenv
from threading import Thread
import RPi.GPIO as GPIO
import sys

load_dotenv() 

# define env variables
HOSTS = os.getenv('HOSTS', '').split(',')
SOUND_URL = os.getenv('SOUND_URL', "https://www.myinstants.com/media/sounds/movie_1.mp3")
GPIO_PIN = os.getenv('GPIO_PIN', 15)
NOTIFIER = pn.PushNotifier(os.getenv('PUSHNOTIFIER_USER', ''), os.getenv('PUSHNOTIFIER_PASSWORD', ''), os.getenv('PUSHNOTIFIER_PACKAGE', ''),  os.getenv('PUSHNOTIFIER_TOKEN'))

print('starting service')
print(HOSTS)

def playSound(host):
    print('DONG')
    try:
        googleDevice = GoogleHome(host=host)
        googleDevice.play(SOUND_URL)
    except:
        pass

def notify(args):
    print('DING')
    if os.getenv('PUSHNOTIFIER_USER', ''):
        NOTIFIER.send_text('ding dong')
    if HOSTS:
        for host in HOSTS:
            thread = Thread(target = playSound, args=[host])
            thread.start()

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(GPIO_PIN, GPIO.RISING, callback=notify)

while True:
    time.sleep(10)