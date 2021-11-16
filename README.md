# google-doorbell


from googlehomepush import GoogleHome
import time 

print('hi')

#GoogleHome(host="192.168.8.120").say("test", 'en')

print('test2')

for host in ["192.168.8.120", "192.168.8.75",  "192.168.8.135", "192.168.8.220"]:
    try:
        googleDevice = GoogleHome(host=host)
        googleDevice.play("https://www.myinstants.com/media/sounds/roblox-death-sound_1.mp3")
    except:
        pass
