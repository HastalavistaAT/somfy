import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

RELAIS_UP_GPIO = 20
RELAIS_DOWN_GPIO = 21

GPIO.setup(RELAIS_UP_GPIO, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(RELAIS_DOWN_GPIO, GPIO.OUT, initial=GPIO.LOW)

time.sleep(5)

GPIO.output(RELAIS_UP_GPIO, GPIO.HIGH)
time.sleep(1)
GPIO.output(RELAIS_UP_GPIO, GPIO.LOW)

GPIO.cleanup()
