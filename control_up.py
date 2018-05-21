import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

RELAIS_UP_GPIO = 20

GPIO.setup(RELAIS_UP_GPIO, GPIO.OUT, initial=GPIO.HIGH)

GPIO.output(RELAIS_UP_GPIO, GPIO.LOW)
time.sleep(0.5)
GPIO.output(RELAIS_UP_GPIO, GPIO.HIGH)

GPIO.cleanup()
