import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

RELAIS_DOWN_GPIO = 21

GPIO.setup(RELAIS_DOWN_GPIO, GPIO.OUT, initial=GPIO.HIGH)

GPIO.output(RELAIS_DOWN_GPIO, GPIO.LOW)
time.sleep(0.5)
GPIO.output(RELAIS_DOWN_GPIO, GPIO.HIGH)

GPIO.cleanup()
