import RPi.GPIO as GPIO
import time
import threading

def startVacuumMotor():
    GPIO.output(motorV_ENA, GPIO.HIGH)
    pwmV.ChangeDutyCycle(100)

def stopvacuumMotor():
    GPIO.output(motorV_ENA, GPIO.LOW)
    pwmV.ChangeDutyCycle(0)

def test_start_stop_vacuunMotor():
    GPIO.output(motorV_ENA, GPIO.LOW)
    pwmV.ChangeDutyCycle(0)

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
    stopvacuumMotor()  # 停止真空馬達

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# vacuum motor
motorV_ENA = 33
GPIO.setup(motorV_ENA, GPIO.OUT)
pwmV = GPIO.PWM(motorV_ENA, 100)
pwmV.start(0)

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
    stopvacuumMotor()  # 確保馬達停止
    GPIO.cleanup()  # 清理 GPIO
    exit()
    pass
finally:
    stopvacuumMotor()  # 確保馬達停止
    GPIO.cleanup()  # 清理 GPIO
    exit()