import RPi.GPIO as GPIO
import time

#mian file
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

#left
motorLIN3 = 3
motorLIN4 = 5
motorLENB = 7 #32 PWM0
GPIO.setup(motorLIN3, GPIO.OUT)
GPIO.setup(motorLIN4, GPIO.OUT)
GPIO.setup(motorLENB, GPIO.OUT)

#right
motorRIN1 = 10
motorRIN2 = 12
motorRENA = 8 #33 PWM1
GPIO.setup(motorRIN1, GPIO.OUT)
GPIO.setup(motorRIN2, GPIO.OUT)
GPIO.setup(motorRENA, GPIO.OUT)

#irSensor
#irSensorL = 11
#irSensorR = 13
#GPIO.setup(irSensorL, GPIO.IN)
#GPIO.setup(irSensorR, GPIO.IN)

#hcrs04
trig = 15
GPIO.setup(trig, GPIO.OUT, initial=GPIO.LOW)
echo = 16
GPIO.setup(echo, GPIO.IN)

#pwm
# pwmL = GPIO.PWM(motorLENB, 100)
# pwmR = GPIO.PWM(motorRENA, 100)
# pwmL.start(0)
# pwmR.start(0)

def forward():
    print('forward')
    time.sleep(1)
    #left
    GPIO.output(motorLIN3, GPIO.LOW)
    GPIO.output(motorLIN4, GPIO.HIGH)
    GPIO.output(motorLENB, GPIO.HIGH)
    # pwmL.ChangeDutyCycle(100)
    #right
    GPIO.output(motorRIN1, GPIO.LOW)
    GPIO.output(motorRIN2, GPIO.HIGH)
    GPIO.output(motorRENA, GPIO.HIGH)
    # pwmR.ChangeDutyCycle(100)
    
def backward():
    print('backward')
    time.sleep(1)
    #left
    GPIO.output(motorLIN3, GPIO.HIGH)
    GPIO.output(motorLIN4, GPIO.LOW)
    GPIO.output(motorLENB, GPIO.HIGH)
    # pwmL.ChangeDutyCycle(100)
    #right
    GPIO.output(motorRIN1, GPIO.HIGH)
    GPIO.output(motorRIN2, GPIO.LOW)
    GPIO.output(motorRENA, GPIO.HIGH)
    # pwmR.ChangeDutyCycle(100)
    
def left():
    print('left')
    time.sleep(1)
    #left
    GPIO.output(motorLIN3, GPIO.HIGH)
    GPIO.output(motorLIN4, GPIO.LOW)
    GPIO.output(motorLENB, GPIO.HIGH)
    # pwmL.ChangeDutyCycle(100)
    #right
    GPIO.output(motorRIN1, GPIO.LOW)
    GPIO.output(motorRIN2, GPIO.HIGH)
    GPIO.output(motorRENA, GPIO.HIGH)
    # pwmR.ChangeDutyCycle(100)
    
def right():
    print('right')
    time.sleep(1)
    #left
    GPIO.output(motorLIN3, GPIO.LOW)
    GPIO.output(motorLIN4, GPIO.HIGH)
    GPIO.output(motorLENB, GPIO.HIGH)
    # pwmL.ChangeDutyCycle(100)
    #right
    GPIO.output(motorRIN1, GPIO.HIGH)
    GPIO.output(motorRIN2, GPIO.LOW)
    GPIO.output(motorRENA, GPIO.HIGH)
    # pwmR.ChangeDutyCycle(100)
    
def stop():
    print('stop')
    time.sleep(1)
    #left
    GPIO.output(motorLIN3, GPIO.LOW)
    GPIO.output(motorLIN4, GPIO.LOW)
    GPIO.output(motorLENB, GPIO.LOW)
    # pwmL.ChangeDutyCycle(0)
    #right
    GPIO.output(motorRIN1, GPIO.LOW)
    GPIO.output(motorRIN2, GPIO.LOW)
    GPIO.output(motorRENA, GPIO.LOW)
    # pwmR.ChangeDutyCycle(0)

    time.sleep(2)
    #left
    GPIO.output(motorLENB, GPIO.LOW)
    #right
    GPIO.output(motorRENA, GPIO.LOW)
    #GPIO.cleanup()

def getdistance():
    GPIO.output(trig, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(trig, GPIO.LOW)
    while not GPIO.input(echo):
        pass
    t1 = time.time()
    while GPIO.input(16):
        pass
    t2 = time.time()
    # print("%.2f" % (((t2-t1)*34300)/2))
    # return ((t2-t1)*34300)/2
    # return "%.2f" % (((t2-t1)*34300)/2)
    return round(((t2-t1)*34300)/2, 2)

# def move_forward(target_speed, step=5, duration=5):
#     current_speed = 0
    
    # GPIO.output(motorLIN3, GPIO.LOW)
    # GPIO.output(motorLIN4, GPIO.HIGH)

    # GPIO.output(motorRIN1, GPIO.LOW)
    # GPIO.output(motorRIN2, GPIO.HIGH)

#     while current_speed < target_speed:
#         current_speed += step
#         if current_speed > target_speed:
#             current_speed = target_speed
#         pwmL.ChangeDutyCycle(current_speed)
#         pwmR.ChangeDutyCycle(current_speed)
#         time.sleep(duration / (target_speed / step))
# move_forward(100)
# time.sleep(3)

# def smooth_deceleration(target_speed, step=5, duration=5):
#     current_speed = target_speed
    
#     while current_speed > 0:
#         current_speed -= step
#         if current_speed < 0:
#             current_speed = 0
#         pwmL.ChangeDutyCycle(current_speed)
#         pwmR.ChangeDutyCycle(current_speed)
#         time.sleep(duration / (target_speed / step))
# smooth_deceleration(100, duration=3)

# def turn_right(speed=50, duration=2):
#     GPIO.output(motorLIN3, GPIO.LOW)
#     GPIO.output(motorLIN4, GPIO.HIGH)
#     GPIO.output(motorRIN1, GPIO.HIGH)
#     GPIO.output(motorRIN2, GPIO.LOW)
    
#     pwmL.ChangeDutyCycle(speed)
#     pwmR.ChangeDutyCycle(speed)

#     time.sleep(duration)

#     pwmL.ChangeDutyCycle(0)
#     pwmR.ChangeDutyCycle(0)
#     GPIO.output(motorLIN3, GPIO.LOW)
#     GPIO.output(motorLIN4, GPIO.LOW)
#     GPIO.output(motorRIN1, GPIO.LOW)
#     GPIO.output(motorRIN2, GPIO.LOW)
# turn_right(speed=50, duration=2)

# def turn_left(speed=50, duration=2):
#     GPIO.output(motorLIN3, GPIO.HIGH)
#     GPIO.output(motorLIN4, GPIO.LOW)
#     GPIO.output(motorRIN1, GPIO.LOW)
#     GPIO.output(motorRIN2, GPIO.HIGH)
    
#     pwmL.ChangeDutyCycle(speed)
#     pwmR.ChangeDutyCycle(speed)

#     time.sleep(duration)

#     pwmL.ChangeDutyCycle(0)
#     pwmR.ChangeDutyCycle(0)
#     GPIO.output(motorLIN3, GPIO.LOW)
#     GPIO.output(motorLIN4, GPIO.LOW)
#     GPIO.output(motorRIN1, GPIO.LOW)
#     GPIO.output(motorRIN2, GPIO.LOW)
# turn_left(speed=50, duration=2)

def loop():
    a = "stop"
    while True:
        if getdistance() > 10:
            # lSensor = GPIO.input(irSensorL)
            #rSensor = GPIO.input(irSensorR)
            #if lSensor == 1 and rSensor == 1:
                if a != "forward":
                    forward()
                    a = "forward"
                    print("is forward")
            #elif lSensor == 0 and rSensor == 1:
                # print("turn left")
            # else:
            # lSensor == 1 and rSensor == 0
                # print("turn right")
        else:
            if a != "stop":
                stop()
                a = "stop"
                print("is stop")
        #exit()
        time.sleep(0.5)


if __name__ == '__main__':
    try:
        loop()
        # exit()
    except KeyboardInterrupt:
       print('Measurement stopped by User')
       GPIO.cleanup
       #pass
    # finally:
        # pwmL.stop()
        # pwmR.stop()
        # GPIO.cleanup