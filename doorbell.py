from googlehomepush import GoogleHome
from pushnotifier import PushNotifier as pn
import time 
import os
from dotenv import load_dotenv
from threading import Thread
import RPi.GPIO as GPIO
from datetime import datetime

load_dotenv() 
## define env variables

# Raspberry Pi GPIO pin that senses for HIGH signal
GPIO_PIN = int(os.getenv('GPIO_PIN', 7))

# Hosts to send a sound to when triggered
HOSTS = os.getenv('HOSTS', '').split(',')
SOUND_URL = os.getenv('SOUND_URL', "https://www.myinstants.com/media/sounds/movie_1.mp3")
DEVICES = os.getenv('DEVICES', None)
if DEVICES:
    DEVICES = DEVICES.split(',')

# Login to PushNotifier for push notifications
if os.getenv('PUSHNOTIFIER_USER', ''):
    NOTIFIER = pn.PushNotifier(os.getenv('PUSHNOTIFIER_USER', ''), os.getenv('PUSHNOTIFIER_PASSWORD', ''), os.getenv('PUSHNOTIFIER_PACKAGE', ''),  os.getenv('PUSHNOTIFIER_TOKEN'))


def playSound(host):
    print('DONG')
    try:
        googleDevice = GoogleHome(host=host)
        googleDevice.play(SOUND_URL)
    except:
        pass

def notify():
    print('DING')
    # Send notifications to all users on PushNotifier account 
    if os.getenv('PUSHNOTIFIER_USER', ''):
        NOTIFIER.send_text('ding dong', devices=DEVICES)

    # Send play requests to Google devices in threads
    if HOSTS:
        for host in HOSTS:
            thread = Thread(target = playSound, args=[host])
            thread.start()


def rc_time (pin_to_circuit):
    count = 0

    #Output on the pin for
    GPIO.setup(pin_to_circuit, GPIO.OUT)
    GPIO.output(pin_to_circuit, GPIO.LOW)
    time.sleep(0.1)

    #Change the pin back to input
    GPIO.setup(pin_to_circuit, GPIO.IN)

    start = time.time_ns()
    GPIO.wait_for_edge(pin_to_circuit, GPIO.RISING)
    end = time.time_ns()

    return end - start

GPIO.setmode(GPIO.BOARD)
print('Starting service..')

#Catch when script is interrupted, cleanup correctly
last_activation = datetime.now()
try:
    # Main loop
    while True:
        if rc_time(GPIO_PIN) < 10000000000 and (datetime.now() - last_activation).seconds > 60:
            last_activation = datetime.now()
            notify()
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()