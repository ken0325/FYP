import RPi.GPIO as GPIO
import time

#hcrs04
def getdistance():
    GPIO.output(trig, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(trig, GPIO.LOW)
    while not GPIO.input(echo):
        pass
    t1 = time.time()
    while GPIO.input(12):
        pass
    t2 = time.time()
    return ((t2-t1)*34300)/2

def loop():
    while True:
        print(f"Distance: {getdistance():.2f} cm")
        time.sleep(0.5)
              
if __name__ == '__main__':
    try:
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        trig = 11
        GPIO.setup(trig, GPIO.OUT, initial=GPIO.LOW)
        echo = 12
        GPIO.setup(echo, GPIO.IN)
        time.sleep(1)
        loop()
    except KeyboardInterrupt:
        GPIO.cleanup()