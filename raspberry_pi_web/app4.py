#latest 23/3/2025
from flask import Flask, render_template, request, jsonify
import RPi.GPIO as GPIO
import time
import threading
from threading import Timer

# GPIO setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

app = Flask(__name__)

# pwm DutyCycle (control motor current, speed)
dutyCycle = 20

vacuumMotorDutyCycle = 100

# driving motor
motorL_IN3 = 3
motorL_IN4 = 5
motorL_ENB = 7
GPIO.setup(motorL_IN3, GPIO.OUT)
GPIO.setup(motorL_IN4, GPIO.OUT)
GPIO.setup(motorL_ENB, GPIO.OUT)
pwmL = GPIO.PWM(motorL_ENB, 100)
pwmL.start(0)
motorR_IN1 = 10
motorR_IN2 = 12
motorR_ENA = 8
GPIO.setup(motorR_IN1, GPIO.OUT)
GPIO.setup(motorR_IN2, GPIO.OUT)
GPIO.setup(motorR_ENA, GPIO.OUT)
pwmR = GPIO.PWM(motorR_ENA, 100)
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

# PWM setup
# pwmL = GPIO.PWM(motorL_ENB, 100)
# pwmR = GPIO.PWM(motorR_ENA, 100)
# pwmV = GPIO.PWM(motorV_ENA, 100)
# pwmL.start(0)
# pwmR.start(0)
# pwmV.start(0)

currentMode = 1
is_pause = False
running_thread = None

# warnings led
is_error = False
LED = 40
GPIO.setup(LED, GPIO.OUT)

def warnings():
    global is_error
    while is_error == True:
        time.sleep(1)
        GPIO.output(LED, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(LED, GPIO.LOW)
        
@app.route('/stopError', methods=['POST'])
def stopWarnings():
    global is_pause, is_error
    if is_pause == True and is_error == True:
        is_error = False
        is_pause = False
        GPIO.output(LED, GPIO.LOW)
        start_vacuum_motor()
        start_motors()
        return jsonify(success=True, message="The operation was successful and normal operation has been resumed.")
    else:
        return jsonify(success=False, message="There is no any errors!")

def start_vacuum_motor():
    pwmV.start(0)
    # print("Start vacuum motor")
    GPIO.output(motorV_ENA, GPIO.HIGH)
    # pwmV.ChangeDutyCycle(100)
    pwmV.ChangeDutyCycle(vacuumMotorDutyCycle)

def stop_vacuum_motor():
    # print("stop vacuum motor")
    GPIO.output(motorV_ENA, GPIO.LOW)
    pwmV.ChangeDutyCycle(0)
    pwmV.stop()

def start_motors():
    pwmL.start(0)
    pwmR.start(0)
    
def stop_motors():
    pwmL.stop()
    pwmR.stop()

def forward():
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
    # print("center distance " + str(d))
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
    # print("left distance " + str(d_L))
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
    # print("right distance " + str(d_R))
    return d_R

def start_initial_function():
    global running_thread
    print("程序啟動，執行按鈕 1 的功能。")
    running_thread = threading.Thread(target=run_function_1)
    running_thread.start()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cleanup')
def cleanup():
    GPIO.cleanup()
    return "GPIO cleaned up!"

@app.route('/start', methods=['POST'])
def start():
    global currentMode, running_thread, is_pause
    if currentMode == 1:        
        if running_thread is not None and running_thread.is_alive():
            running_thread.join()
            
        running_thread = threading.Thread(target=run_function_1)
        running_thread.start()
        is_pause = False
        return jsonify(success=True, message="The mode 1 we be continue.")
    elif currentMode == 2:
        if running_thread is not None and running_thread.is_alive():
            running_thread.join()
            
        running_thread = threading.Thread(target=run_function_2)
        running_thread.start()
        is_pause = False
        return jsonify(success=True, message="The mode 2 we be continue.")
    else:
        return jsonify(success=False, message="Can't continue, please check!")

@app.route('/pause', methods=['POST'])
def pasuse():
    global is_pause
    stop_motors()
    stop_vacuum_motor()
    is_pause = True
    return jsonify(success=True, message="The robot is stopped.")

@app.route('/vacuum', methods=['POST'])
def set_control_vacuum():
    global vacuumMotorDutyCycle
    power = request.form.get('power', type=int)
    if power is not None:
        vacuumMotorDutyCycle = power
        # pwmV.ChangeDutyCycle(0 if power == 49 else power)
        pwmV.ChangeDutyCycle(power)
        return jsonify(success=True, message="The vacuum power is changed.")
    else:
        return jsonify(success=False, message="Some wrong, please check!")

@app.route('/startVacuum')
def startVacuum():
    start_vacuum_motor()
    return jsonify(success=True, message="The vacuum is started.")

@app.route('/stopVacuum')
def stopVacuum():
    stop_vacuum_motor()
    return jsonify(success=True, message="The vacuum is stopped.")

@app.route('/changeToMode1', methods=['POST'])
def mode1Btn_callback():
    global currentMode, running_thread
    if currentMode != 1:
        currentMode = 1
        stop()
        
        if running_thread is not None and running_thread.is_alive():
            running_thread.join()
            
        running_thread = threading.Thread(target=run_function_1)
        running_thread.start()
        return jsonify(success=True, message="Will change to mode 1")
    else:
        return jsonify(success=False, message="Mode 1 is already")

@app.route('/changeToMode2', methods=['POST'])
def mode2Btn_callback():
    global currentMode, running_thread
    if currentMode != 2:
        currentMode = 2
        stop()
        print("change current mode to 2")
        
        if running_thread is not None and running_thread.is_alive():
            running_thread.join()
            
        running_thread = threading.Thread(target=run_function_2)
        running_thread.start()
        return jsonify(success=True, message="Will change to mode 2")
    else:
        return jsonify(success=False, message="Mode 2 is already")

distance_data = []
def measure_distance(fDistance, leftDistance, rightDistance):
    global is_pause, is_error
    distance_data.append(fDistance)
    distance_data.append(leftDistance)
    distance_data.append(rightDistance)
    # t = threading.Timer(60, measure_distance)
    if distance_data and is_error == False:
        average_distance = sum(distance_data) / len(distance_data)
        if average_distance <= 10:
            print('error: avgDistance ', average_distance)
            stop_motors()
            stop_vacuum_motor()
            is_pause = True
            is_error = True
        if len(distance_data) >= 30:
            distance_data.clear()
        
        # Timer(60, measure_distance).start()
        # t.start()
    # else:
        # t.cancel()
        

def mode1():
    global is_pause
    # stop forward backward left right
    current_state = ""
    while currentMode == 1 and is_pause == False:
        distanceF = getdistance()
        distanceL = getdistanceleft()
        distanceR = getdistanceright()
        # print("\n" + current_state)
        time.sleep(1)
        measure_distance(distanceF, distanceL, distanceR)
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
                
def mode2():
    global is_pause
    current_state = ""
    while currentMode == 2 and is_pause == False:
        distanceF = getdistance()
        distanceL = getdistanceleft()
        distanceR = getdistanceright()
        maxDistance = 0
        
        if (distanceF > distanceL) and (distanceF > distanceR):
            print('forward')
            maxDistance = distanceF
            forward()
            current_state = "forward"
        elif (distanceL > distanceF) and (distanceL > distanceR):
            print('left')
            maxDistance = distanceL
            left()
            current_state = "left"
        else:
            print('right')
            maxDistance = distanceR
            right()
            current_state = "right"
            
        if maxDistance > 50:
            target_speed = 100  # 距離大於50 cm時，設定最大速度
        elif maxDistance > 30:
            target_speed = 70   # 距離在30-50 cm之間，設定較低速度
        elif maxDistance > 10:
            target_speed = 30   # 距離在10-30 cm之間，設定更低速度
        else:
            target_speed = 0    # 距離小於10 cm時，停止

        # 平滑調整速度
        if current_speed < target_speed:
            current_speed += 5  # 每次增加5%
        elif current_speed > target_speed:
            current_speed -= 5  # 每次減少5%

        # 確保速度在0到100範圍內
        current_speed = max(0, min(100, current_speed))
        
        pwmL.ChangeDutyCycle(current_speed)  # 更新PWM信號
        pwmR.ChangeDutyCycle(current_speed)  # 更新PWM信號
        
        time.sleep(0.1)

def run_function_1():
    print('this is mode1')
    start_motors()
    start_vacuum_motor()
    time.sleep(1)
    mode1()

def run_function_2():
    print('this is mode 2')
    start_motors()
    start_vacuum_motor()
    time.sleep(1)
    mode2()

if __name__ == '__main__':
    start_initial_function()
    
    try:
        app.run(host='0.0.0.0', port=5000)
    except KeyboardInterrupt:
        print('Measurement stopped by User')
        stop_motors()
        stop_vacuum_motor()
        GPIO.cleanup()
        exit()
        pass
    finally:
        stop_motors()
        stop_vacuum_motor()
        GPIO.cleanup()
        exit()