#latest 1/6/2025
import RPi.GPIO as GPIO
import time

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
    # k = True
    while x<=10:
        distanceF = getdistance()
        distanceL = getdistanceleft()
        distanceR = getdistanceright()
        print("\n" + current_state)
        print("\n" + str(x))
        time.sleep(1)
        
        if distanceF <= 20 or distanceL <= 20 or distanceR <= 20:
            x+=1
            if distanceF <= 20:
                if distanceL <= 20 and distanceR <= 20:
                    #print('backward')
                    if current_state != "backward":
                        stop()
                        time.sleep(1)
                        backward()
                        current_state = "backward"
                elif distanceL <= 20:
                    #print('right')
                    if current_state != "right":
                        stop()
                        time.sleep(1)
                        right()
                        current_state = "right"
                else:
                    #print('left')
                    if current_state != "left":
                        stop()
                        time.sleep(1)
                        left()
                        current_state = "left"
            elif distanceR <= 20:
                if distanceL <= 20:
                    #print('backward')
                    if current_state != "backward":
                        stop()
                        time.sleep(1)
                        backward()
                        current_state = "backward"
                else:
                    #print('left')
                    if current_state != "left":
                        stop()
                        time.sleep(1)
                        left()
                        current_state = "left"
            elif distanceL <= 20:
                if distanceR <= 20:
                    #print('backward')
                    if current_state != "backward":
                        stop()
                        time.sleep(1)
                        backward()
                        current_state = "backward"
                else:
                    #print('right')
                    if current_state != "right":
                        stop()
                        time.sleep(1)
                        right()
                        current_state = "right"
        else:
            #print('forward')
            if current_state != "forward":
                stop()
                time.sleep(1)
                forward()
                current_state = "forward"

if __name__ == '__main__':
    try:

        #mian file
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        dutyCycle = 13
        
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
        
def moveingByDistance():
    df = getdistance()
    dl = getdistanceleft()
    dr = getdistanceright()
    
    if (df < dl) and (df < dr):
        smallest_num = df
        # forward()
    elif (dl < df) and (dl < dr):
        smallest_num = dl
        # left()
    else:
        smallest_num = dr
        # right()
        
def changeMode():
    # test
    # mode 1 = auto, 2 = , 3 = 
    mode = 1
    mode1Btn = 36
    mode2Btn = 38
    mode3Btn = 40
    GPIO.setup(mode1Btn, GPIO.IN)
    GPIO.setup(mode2Btn, GPIO.IN)
    GPIO.setup(mode3Btn, GPIO.IN)
    if (GPIO.input(mode1Btn) == True): 
        mode = 1
    elif (GPIO.input(mode2Btn) == True): 
        mode = 2
    else:
        mode = 3
        
    if (mode == 1):
        mode = 1
    elif (mode == 2):
        mode = 2
    else:
        mode = 3