import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

trig = 15
GPIO.setup(trig, GPIO.OUT, initial=GPIO.LOW)
echo = 16
GPIO.setup(echo, GPIO.IN)

for i in range(5):
    GPIO.output(trig, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(trig, GPIO.LOW)
    while not GPIO.input(echo):
        pass
    t1 = time.time()
    while GPIO.input(16):
        pass
    t2 = time.time()
    d = round(((t2-t1)*34300)/2, 2)
    # print(d)
    print("center distance " + str(d))
    time.sleep(1)