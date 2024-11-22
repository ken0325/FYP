# Testing GPIO
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)

#i=0

GPIO.setmode(GPIO.BOARD)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(3, GPIO.IN)

#while i <= 5:
#    GPIO.output(22, GPIO.HIGH)
#    time.sleep(1)
#    GPIO.output(22, GPIO.LOW)
#    time.sleep(1)
#    i += 1
while True:
    if (GPIO.input(3)==False):
        time.sleep(1)
        GPIO.output(22, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(22, GPIO.LOW)
    if (GPIO.input(3)==True):
        time.sleep(0.5)
        GPIO.output(22, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(22, GPIO.LOW)

exit()
