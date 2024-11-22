# Motor Control
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

#left
motorLIN3 = 3
motorLIN4 = 5
motorLENB = 7
GPIO.setup(motorLIN3, GPIO.OUT)
GPIO.setup(motorLIN4, GPIO.OUT)
GPIO.setup(motorLENB, GPIO.OUT)

#right
motorRIN1 = 38
motorRIN2 = 40
motorRENA = 36
GPIO.setup(motorRIN1, GPIO.OUT)
GPIO.setup(motorRIN2, GPIO.OUT)
GPIO.setup(motorRENA, GPIO.OUT)

def test():
    print("import file")

def forward():
    print('forward')
    GPIO.output(motorLIN3, GPIO.LOW)
    GPIO.output(motorLIN4, GPIO.HIGH)
    GPIO.output(motorLENB, GPIO.HIGH)
    GPIO.output(motorRIN1, GPIO.HIGH)
    GPIO.output(motorRIN2, GPIO.LOW)
    GPIO.output(motorRENA, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(motorLENB, GPIO.LOW)
    GPIO.output(motorRENA, GPIO.LOW)

    
def backward():
    print('backward')
    GPIO.output(motorLIN3, GPIO.HIGH)
    GPIO.output(motorLIN4, GPIO.LOW)
    GPIO.output(motorLENB, GPIO.HIGH)
    GPIO.output(motorRIN1, GPIO.LOW)
    GPIO.output(motorRIN2, GPIO.HIGH)
    GPIO.output(motorRENA, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(motorLENB, GPIO.LOW)
    GPIO.output(motorRENA, GPIO.LOW)
    
def left():
    print('left')
    GPIO.output(motorLIN3, GPIO.HIGH)
    GPIO.output(motorLIN4, GPIO.LOW)
    GPIO.output(motorLENB, GPIO.HIGH)
    GPIO.output(motorRIN1, GPIO.HIGH)
    GPIO.output(motorRIN2, GPIO.LOW)
    GPIO.output(motorRENA, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(motorLENB, GPIO.LOW)
    GPIO.output(motorRENA, GPIO.LOW)

def right():
    print('right')
    GPIO.output(motorLIN3, GPIO.LOW)
    GPIO.output(motorLIN4, GPIO.HIGH)
    GPIO.output(motorLENB, GPIO.HIGH)
    GPIO.output(motorRIN1, GPIO.LOW)
    GPIO.output(motorRIN2, GPIO.HIGH)
    GPIO.output(motorRENA, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(motorLENB, GPIO.LOW)
    GPIO.output(motorRENA, GPIO.LOW)
    
def stop():
    print('stop')
    GPIO.output(motorLIN3, GPIO.LOW)
    GPIO.output(motorLIN4, GPIO.LOW)
    GPIO.output(motorLENB, GPIO.LOW)
    GPIO.output(motorRIN1, GPIO.LOW)
    GPIO.output(motorRIN2, GPIO.LOW)
    GPIO.output(motorRENA, GPIO.LOW)
    time.sleep(2)
    GPIO.output(motorLENB, GPIO.LOW)
    GPIO.output(motorRENA, GPIO.LOW)
    
#right()
#stop()

#print('Now stop')
#GPIO.cleanup()