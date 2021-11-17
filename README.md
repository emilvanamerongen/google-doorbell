# google-doorbell

Script to play a sound on google home devices and/or send push notifications when triggering a raspberry pi GPIO pin.

## How to use

### install requirements

```bash
pip3 install -r requirements.txt
```

### Raspberry pi sensor pin

```.env file
GPIO_PIN=17
```
### Google home sounds

Add hosts to send sound to as comma seperated list:


```.env file
HOSTS="192.168.1.1,192.168.1.2"
```

### Push notifications

Connect a pushnotifier account using the following env variables:

```.env file
PUSHNOTIFIER_TOKEN="XXXX"
PUSHNOTIFIER_PACKAGE="com.myapp.app"
PUSHNOTIFIER_USER="username"
PUSHNOTIFIER_PASSWORD="password"
```