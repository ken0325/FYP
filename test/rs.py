#latest 1/10/2025
import RPi.GPIO as GPIO
import time
import threading

def vacuumMotor():
    print('Start vacuum motor')
    GPIO.output(motorV_IN1, GPIO.LOW)
    GPIO.output(motorV_IN2, GPIO.HIGH)
    GPIO.output(motorV_ENA, GPIO.HIGH)
    pwmV.ChangeDutyCycle(10)

def forward():
    print('forward')
    #left
    GPIO.output(motorL_IN3, GPIO.LOW)
    GPIO.output(motorL_IN4, GPIO.HIGH)
    GPIO.output(motorL_ENB, GPIO.HIGH)
    pwmL.ChangeDutyCycle(dutyCycle)
    #right
    GPIO.output(motorR_IN1, GPIO.LOW)
    GPIO.output(motorR_IN2, GPIO.HIGH)
    GPIO.output(motorR_ENA, GPIO.HIGH)
    pwmR.ChangeDutyCycle(dutyCycle)
    
def backward():
    print('backward')
    #left
    GPIO.output(motorL_IN3, GPIO.HIGH)
    GPIO.output(motorL_IN4, GPIO.LOW)
    GPIO.output(motorL_ENB, GPIO.HIGH)
    pwmL.ChangeDutyCycle(dutyCycle)
    #right
    GPIO.output(motorR_IN1, GPIO.HIGH)
    GPIO.output(motorR_IN2, GPIO.LOW)
    GPIO.output(motorR_ENA, GPIO.HIGH)
    pwmR.ChangeDutyCycle(dutyCycle)
    
def left():
    print('left')
    #left
    GPIO.output(motorL_IN3, GPIO.HIGH)
    GPIO.output(motorL_IN4, GPIO.LOW)
    GPIO.output(motorL_ENB, GPIO.HIGH)
    pwmL.ChangeDutyCycle(dutyCycle)
    #right
    GPIO.output(motorR_IN1, GPIO.LOW)
    GPIO.output(motorR_IN2, GPIO.HIGH)
    GPIO.output(motorR_ENA, GPIO.HIGH)
    pwmR.ChangeDutyCycle(dutyCycle)
    
def right():
    print('right')
    #left
    GPIO.output(motorL_IN3, GPIO.LOW)
    GPIO.output(motorL_IN4, GPIO.HIGH)
    GPIO.output(motorL_ENB, GPIO.HIGH)
    pwmL.ChangeDutyCycle(dutyCycle)
    #right
    GPIO.output(motorR_IN1, GPIO.HIGH)
    GPIO.output(motorR_IN2, GPIO.LOW)
    GPIO.output(motorR_ENA, GPIO.HIGH)
    pwmR.ChangeDutyCycle(dutyCycle)
    
def stop():
    print('stop')
    #left
    GPIO.output(motorL_IN3, GPIO.LOW)
    GPIO.output(motorL_IN4, GPIO.LOW)
    GPIO.output(motorL_ENB, GPIO.LOW)
    pwmL.ChangeDutyCycle(0)
    #right
    GPIO.output(motorR_IN1, GPIO.LOW)
    GPIO.output(motorR_IN2, GPIO.LOW)
    GPIO.output(motorR_ENA, GPIO.LOW)
    pwmR.ChangeDutyCycle(0)

    #left
    GPIO.output(motorL_ENB, GPIO.LOW)
    #right
    GPIO.output(motorR_ENA, GPIO.LOW)
                
# 
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# pwm DutyCycle (control motor current, speed)
dutyCycle = 13

# left motor
motorL_IN3 = 3
motorL_IN4 = 5
motorL_ENB = 7
GPIO.setup(motorL_IN3, GPIO.OUT)
GPIO.setup(motorL_IN4, GPIO.OUT)
GPIO.setup(motorL_ENB, GPIO.OUT)

# right motor
motorR_IN1 = 10
motorR_IN2 = 12
motorR_ENA = 8
GPIO.setup(motorR_IN1, GPIO.OUT)
GPIO.setup(motorR_IN2, GPIO.OUT)
GPIO.setup(motorR_ENA, GPIO.OUT)

pwmL = GPIO.PWM(motorL_ENB, 100)
pwmR = GPIO.PWM(motorR_ENA, 100)
pwmL.start(0)
pwmR.start(0)

# test vacuum motor
motorV_IN1 = 35
motorV_IN2 = 37
motorV_ENA = 33
GPIO.setup(motorV_IN1, GPIO.OUT)
GPIO.setup(motorV_IN2, GPIO.OUT)
GPIO.setup(motorV_ENA, GPIO.OUT)
pwmV = GPIO.PWM(motorV_ENA, 100)
pwmV.start(0)
# test b

        
try:

    
    pwmL.stop()
    pwmR.stop()
    pwmV.stop()
    GPIO.cleanup
    time.sleep(1)
    exit()
except KeyboardInterrupt:
    print('Measurement stopped by User')
    #GPIO.cleanup()
    pass
finally:
    GPIO.cleanup()
