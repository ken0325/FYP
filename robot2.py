#latest 1/27/2025
import RPi.GPIO as GPIO
import time
import threading

def vacuumMotor():
    print('Start vacuum motor')
    GPIO.output(motorV_IN1, GPIO.LOW)
    GPIO.output(motorV_IN2, GPIO.HIGH)
    GPIO.output(motorV_ENA, GPIO.HIGH)
    pwmV.ChangeDutyCycle(vacuumMotorDutyCycle)

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
    while True:
        distanceF = getdistance()
        distanceL = getdistanceleft()
        distanceR = getdistanceright()
        print("\n" + current_state)
        time.sleep(1)
        
        if distanceF <= 20 or distanceL <= 20 or distanceR <= 20:
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
                

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# pwm DutyCycle (control motor current, speed)
dutyCycle = 25
vacuumMotorDutyCycle = 100

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

# vacuum motor
motorV_IN1 = 35
motorV_IN2 = 37
motorV_ENA = 33
GPIO.setup(motorV_IN1, GPIO.OUT)
GPIO.setup(motorV_IN2, GPIO.OUT)
GPIO.setup(motorV_ENA, GPIO.OUT)
pwmV = GPIO.PWM(motorV_ENA, 100)
pwmV.start(0)

# hcrs04
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

# mode button
mode1Btn = 32
mode2Btn = 36
GPIO.setup(mode1Btn, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(mode2Btn, GPIO.IN, pull_up_down=GPIO.PUD_UP)
currentMode = 1
running_thread = None

def start_initial_function():
    global running_thread
    print("程序啟動，執行按鈕 1 的功能。")
    running_thread = threading.Thread(target=run_button_1_function)
    running_thread.start()

def mode1Btn_callback(channel):
    global currentMode, running_thread
    if currentMode != 1:
        currentMode = 1
        print("change current mode to 1")
        
        if running_thread is not None and running_thread.is_alive():
            running_thread.join()
            
        running_thread = threading.Thread(target=run_button_1_function)
        running_thread.start()
    else:
        print('button 1 function already')
        return
    
def run_button_1_function():
    print('button 1 function')
    vacuumMotor()
    time.sleep(1)
    loop()
        
def mode2Btn_callback(channel):
    global currentMode, running_thread
    if currentMode != 2:
        currentMode = 2
        print("change current mode to 2")
        
        if running_thread is not None and running_thread.is_alive():
            running_thread.join()
            
        running_thread = threading.Thread(target=run_button_2_function)
        running_thread.start()
    else:
        print('button 2 function already')
        return
    
def run_button_2_function():
    print('button 2 function')
    # vacuumMotorDutyCycle = 50
    pwmL.stop()
    pwmR.stop()
    pwmV.stop()
    GPIO.cleanup
    time.sleep(1)
    exit()
        
try:
    GPIO.add_event_detect(mode1Btn, GPIO.FALLING, callback=mode1Btn_callback, bouncetime=300)
    GPIO.add_event_detect(mode2Btn, GPIO.FALLING, callback=mode2Btn_callback, bouncetime=300)
    
    start_initial_function()
    
    # print("go, ctrl+c")
    while True:
        time.sleep(1)

    # loop()
    # forward()
    # time.sleep(2)
    # backward()
    # time.sleep(2)
    # right()
    # time.sleep(2)
    # left()
    # time.sleep(2)
    # stop()
    # time.sleep(2)
    
except KeyboardInterrupt:
    print('Measurement stopped by User')
    pwmL.stop()
    pwmR.stop()
    pwmV.stop()
    GPIO.cleanup()
    time.sleep(1)
    exit()
    pass
finally:
    pwmL.stop()
    pwmR.stop()
    pwmV.stop()
    GPIO.cleanup()
    time.sleep(1)
    exit()
        
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