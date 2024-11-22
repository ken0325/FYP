import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(8, GPIO.IN)

while True:
    time.sleep(0.5)
    sensor=GPIO.input(8)
    if sensor==1:
        print("have")
    elif sensor==0:
        print("not have")