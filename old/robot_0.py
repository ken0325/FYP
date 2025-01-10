import RPi.GPIO as GPIO
import time

def forward():
    print('forward')
    #left
    GPIO.output(motorL_IN3, GPIO.LOW)
    GPIO.output(motorL_IN4, GPIO.HIGH)
    GPIO.output(motorL_ENB, GPIO.HIGH)
    #right
    GPIO.output(motorR_IN1, GPIO.HIGH)
    GPIO.output(motorR_IN2, GPIO.LOW)
    GPIO.output(motorR_ENA, GPIO.HIGH)
    
def backward():
    print('backward')
    #left
    GPIO.output(motorL_IN3, GPIO.HIGH)
    GPIO.output(motorL_IN4, GPIO.LOW)
    GPIO.output(motorL_ENB, GPIO.HIGH)
    #right
    GPIO.output(motorR_IN1, GPIO.LOW)
    GPIO.output(motorR_IN2, GPIO.HIGH)
    GPIO.output(motorR_ENA, GPIO.HIGH)
    
def left():
    print('left')
    #left
    GPIO.output(motorL_IN3, GPIO.HIGH)
    GPIO.output(motorL_IN4, GPIO.LOW)
    GPIO.output(motorL_ENB, GPIO.HIGH)
    #right
    GPIO.output(motorR_IN1, GPIO.HIGH)
    GPIO.output(motorR_IN2, GPIO.LOW)
    GPIO.output(motorR_ENA, GPIO.HIGH)
    
def right():
    print('right')
    #left
    GPIO.output(motorL_IN3, GPIO.LOW)
    GPIO.output(motorL_IN4, GPIO.HIGH)
    GPIO.output(motorL_ENB, GPIO.HIGH)
    #right
    GPIO.output(motorR_IN1, GPIO.LOW)
    GPIO.output(motorR_IN2, GPIO.HIGH)
    GPIO.output(motorR_ENA, GPIO.HIGH)
    
def stop():
    print('stop')
    #left
    GPIO.output(motorL_IN3, GPIO.LOW)
    GPIO.output(motorL_IN4, GPIO.LOW)
    GPIO.output(motorL_ENB, GPIO.LOW)
    #right
    GPIO.output(motorR_IN1, GPIO.LOW)
    GPIO.output(motorR_IN2, GPIO.LOW)
    GPIO.output(motorR_ENA, GPIO.LOW)

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
    # stop forward backward turnleft turnright
    current_state = ""
    k = True
    while k:
        distanceF = getdistance()
        distanceL = getdistanceleft()
        distanceR = getdistanceright()
        print("\n" + current_state)
        time.sleep(1)
        
        if distanceF <= 20 or distanceL <= 20 or distanceR <= 20:
            if distanceF <= 20:
                if distanceL <= 20 and distanceR <= 20:
                    print('backward')
                elif distanceL <= 20:
                    print('right')
                else:
                    print('left')
            elif distanceR <= 20:
                if distanceL <= 20:
                    print('backward')
                else:
                    print('left')
            elif distanceL <= 20:
                if distanceR <= 20:
                    print('backward')
                else:
                    print('right')
        else:
            print('forward')
        #if distanceF <= 20 or distanceL <= 20 or distanceR <= 20:
        #    if current_state != "stop":
        #        stop()
        #        current_state = "stop"
                #user_input = input("Do you want to exit the program? (y/n): ")
                #if user_input.lower() == "y":
                #    k = False
                #else:
                #    k = True
        #    else:
        #        if distanceL <= 20 and distanceR <= 20:
        #            backward()
        #            current_state = "backward"
        #        elif distanceL <= 20:
        #            right()
        #            current_state = "right"
        #        else:
        #            left()
        #            current_state = "left"
        #else:
        #    forward()
        #    current_state = "forward"
        
#         if distanceF <= 20:
#             stop()
#             current_state = "stop"
#             if distanceL <= 20:
#                 if distanceR <= 20:
#                     backward()
#                     current_state = "backward"
#                 else:
#                     right()
#                     current_state = "right"
#             else:
#                 left()
#                 current_state = "left"
#         else:
#             forward()
#             current_state = "forward"


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

        #forward()
        #time.sleep(2)
        #stop()
        exit()
        #time.sleep(1)
        # exit()
    except KeyboardInterrupt:
       print('Measurement stopped by User')
       GPIO.cleanup()
       #pass
    # finally:
        # GPIO.cleanup