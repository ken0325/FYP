#latest 1/10/2025
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)

GPIO.cleanup
GPIO.setmode(GPIO.BOARD)
Button = 36
LED = 40
GPIO.setup(Button,GPIO.IN)
GPIO.setup(LED, GPIO.OUT)

while True:
    print(GPIO.input(Button))
    if (GPIO.input(Button)==True):
        time.sleep(1)
        GPIO.output(LED, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(LED, GPIO.LOW)

exit()
