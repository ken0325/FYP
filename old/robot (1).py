import RPi.GPIO as GPIO
import time

def forward():
    print('forward')
    #left
    GPIO.output(motorL_IN3, GPIO.LOW)
    GPIO.output(motorL_IN4, GPIO.HIGH)
    GPIO.output(motorL_ENB, GPIO.HIGH)
    pwmL.ChangeDutyCycle(15)
    #right
    GPIO.output(motorR_IN1, GPIO.LOW)
    GPIO.output(motorR_IN2, GPIO.HIGH)
    GPIO.output(motorR_ENA, GPIO.HIGH)
    pwmR.ChangeDutyCycle(15)
    
def backward():
    print('backward')
    #left
    GPIO.output(motorL_IN3, GPIO.HIGH)
    GPIO.output(motorL_IN4, GPIO.LOW)
    GPIO.output(motorL_ENB, GPIO.HIGH)
    pwmL.ChangeDutyCycle(15)
    #right
    GPIO.output(motorR_IN1, GPIO.HIGH)
    GPIO.output(motorR_IN2, GPIO.LOW)
    GPIO.output(motorR_ENA, GPIO.HIGH)
    pwmR.ChangeDutyCycle(15)
    
def left():
    print('left')
    #left
    GPIO.output(motorL_IN3, GPIO.HIGH)
    GPIO.output(motorL_IN4, GPIO.LOW)
    GPIO.output(motorL_ENB, GPIO.HIGH)
    pwmL.ChangeDutyCycle(15)
    #right
    GPIO.output(motorR_IN1, GPIO.LOW)
    GPIO.output(motorR_IN2, GPIO.HIGH)
    GPIO.output(motorR_ENA, GPIO.HIGH)
    pwmR.ChangeDutyCycle(15)
    
def right():
    print('right')
    #left
    GPIO.output(motorL_IN3, GPIO.LOW)
    GPIO.output(motorL_IN4, GPIO.HIGH)
    GPIO.output(motorL_ENB, GPIO.HIGH)
    pwmL.ChangeDutyCycle(15)
    #right
    GPIO.output(motorR_IN1, GPIO.HIGH)
    GPIO.output(motorR_IN2, GPIO.LOW)
    GPIO.output(motorR_ENA, GPIO.HIGH)
    pwmR.ChangeDutyCycle(15)
    
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
    d = round(((t2-t1)*34300)/2, 2)
    # print(d)
    print("center distance " + str(d))
    return d

def getdistanceleft():
    GPIO.output(trig_L, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(trig_L, GPIO.LOW)
    while not GPIO.input(echo_L):
        pass
    t1 = time.time()
    while GPIO.input(22):
        pass
    t2 = time.time()
    d_L = round(((t2-t1)*34300)/2, 2)
    # print(d_L)
    print("left distance " + str(d_L))
    return d_L

def getdistanceright():
    GPIO.output(trig_R, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(trig_R, GPIO.LOW)
    while not GPIO.input(echo_R):
        pass
    t1 = time.time()
    while GPIO.input(24):
        pass
    t2 = time.time()
    d_R = round(((t2-t1)*34300)/2, 2)
    # print(d_R)
    print("right distance " + str(d_R))
    return d_R

def loop():
    # stop forward backward left right
    current_state = ""
    x=0
    k = True
    while k:
        distanceF = getdistance()
        distanceL = getdistanceleft()
        distanceR = getdistanceright()
        print("\n" + current_state)
        print("\n" + str(x))
        time.sleep(0.3)
        
        if distanceF <= 15 or distanceL <= 15 or distanceR <= 15:
#             x+=1
#             stop()
#             current_state = "stop"
#             time.sleep(1)
            if distanceF <= 15:
                if distanceL <= 15 and distanceR <= 15:
                    #print('backward')
                    if current_state != "backward":
#                         stop()
#                         time.sleep(1)
                        backward()
                        current_state = "backward"
                        time.sleep(0.5)
                elif distanceL <= 15:
                    #print('right')
                    if current_state != "right":
#                         stop()
#                         time.sleep(1)
                        right()
                        current_state = "right"
                        time.sleep(0.5)
                else:
                    #print('left')
                    if current_state != "left":
#                         stop()
#                         time.sleep(1)
                        left()
                        current_state = "left"
                        time.sleep(0.5)
            elif distanceR <= 15:
                if distanceL <= 15:
                    #print('backward')
                    if current_state != "backward":
#                         stop()
#                         time.sleep(1)
                        backward()
                        current_state = "backward"
                        time.sleep(0.5)
                else:
                    #print('left')
                    if current_state != "left":
#                         stop()
#                         time.sleep(1)
                        left()
                        current_state = "left"
                        time.sleep(0.5)
            elif distanceL <= 15:
                if distanceR <= 15:
                    #print('backward')
                    if current_state != "backward":
#                         stop()
#                         time.sleep(1)
                        backward()
                        current_state = "backward"
                        time.sleep(0.5)
                else:
                    #print('right')
                    if current_state != "right":
#                         stop()
#                         time.sleep(1)
                        right()
                        current_state = "right"
                        time.sleep(0.5)
        else:
            #print('forward')
#             stop()
#             time.sleep(1)
            if current_state != "forward":
#                 stop()
#                 time.sleep(1)
                forward()
                current_state = "forward"
                time.sleep(0.5)

if __name__ == '__main__':
    try:

        #mian file
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)

        #left
        motorL_IN3 = 3
        motorL_IN4 = 5
        motorL_ENB = 7
        GPIO.setup(motorL_IN3, GPIO.OUT)
        GPIO.setup(motorL_IN4, GPIO.OUT)
        GPIO.setup(motorL_ENB, GPIO.OUT)

        #right
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

        #hcrs04
        trig = 15
        GPIO.setup(trig, GPIO.OUT, initial=GPIO.LOW)
        echo = 16
        GPIO.setup(echo, GPIO.IN)
        
        trig_L = 21
        GPIO.setup(trig_L, GPIO.OUT, initial=GPIO.LOW)
        echo_L = 22
        GPIO.setup(echo_L, GPIO.IN)
        
        trig_R = 23
        GPIO.setup(trig_R, GPIO.OUT, initial=GPIO.LOW)
        echo_R = 24
        GPIO.setup(echo_R, GPIO.IN)

        time.sleep(1)
        loop()
        
#         forward()
#         time.sleep(2)
#         backward()
#         time.sleep(2)
#         right()
#         time.sleep(2)
#         left()
#         time.sleep(2)
        stop()
        time.sleep(2)
        pwmL.stop()
        pwmR.stop()
        GPIO.cleanup
        time.sleep(1)
        exit()
    except KeyboardInterrupt:
       print('Measurement stopped by User')
       #GPIO.cleanup()
       pass
    finally:
        GPIO.cleanup