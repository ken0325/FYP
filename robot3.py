#latest 2/9/2025
import RPi.GPIO as GPIO
import time
import threading

def startVacuumMotor():
    GPIO.output(motorV_ENA, GPIO.HIGH)
    pwmV.ChangeDutyCycle(100)
    
def stopVacuumMotor():
    GPIO.output(motorV_ENA, GPIO.LOW)
    pwmV.ChangeDutyCycle(0)
    
def test_start_stop_vacuunMotor():
    print('test start stop vacuum motor')
    startVacuumMotor()
    time.sleep(2)
    stopVacuumMotor()
    
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
    pwmL.ChangeDutyCycle(dutyCycle)
    #right
    GPIO.output(motorR_IN1, GPIO.LOW)
    GPIO.output(motorR_IN2, GPIO.LOW)
    GPIO.output(motorR_ENA, GPIO.LOW)
    pwmR.ChangeDutyCycle(dutyCycle)

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
    # while True:
    while currentMode == 1:
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
    startVacuumMotor()
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
    global dutyCycle
    print('button 2 function')
    dutyCycle = 0
    stop()
    pwmL.stop()
    pwmR.stop()
    
    time.sleep(1)
    stopVacuumMotor()

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# pwm DutyCycle (control motor current, speed)
dutyCycle = 25

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
motorV_ENA = 33
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
        
try:
    GPIO.add_event_detect(mode1Btn, GPIO.FALLING, callback=mode1Btn_callback, bouncetime=300)
    GPIO.add_event_detect(mode2Btn, GPIO.FALLING, callback=mode2Btn_callback, bouncetime=300)
    
    start_initial_function()
    
    while True:
        time.sleep(1)
    
except KeyboardInterrupt:
    print('Measurement stopped by User')
    dutyCycle = 0
    stop()
    pwmL.stop()
    pwmR.stop()
    stopVacuumMotor()  # 確保馬達停止
    GPIO.cleanup()  # 清理 GPIO
    exit()
    pass
finally:
    dutyCycle = 0
    stop()
    pwmL.stop()
    pwmR.stop()
    stopVacuumMotor()
    GPIO.cleanup()
    exit()