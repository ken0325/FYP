#latest 1/10/2025
import RPi.GPIO as GPIO
import time
import threading

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

mode1Btn = 32
mode2Btn = 36
GPIO.setup(mode1Btn, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(mode2Btn, GPIO.IN, pull_up_down=GPIO.PUD_UP)

currentMode = None
running_thread = None

def mode1Btn_callback(channel):
    global currentMode, running_thread
    if currentMode != 1:
        currentMode = 1
        print("")
        
        if running_thread is not None and running_thread.is_alive():
            running_thread.join()
            
        running_thread = threading.Thread(target=run_button_1_function)
        running_thread.start()
    else:
        print('already')
        return
    
def run_button_1_function():
    k = 0
    while currentMode == 1:
        print("k", k)
        k += 2
        time.sleep(1)
        
def mode2Btn_callback(channel):
    global currentMode, running_thread
    if currentMode != 2:
        currentMode = 2
        print("")
        
        if running_thread is not None and running_thread.is_alive():
            running_thread.join()
            
        running_thread = threading.Thread(target=run_button_2_function)
        running_thread.start()
    else:
        print('already')
        return
    
def run_button_2_function():
    n = 0
    while currentMode == 2:
        print("n", n)
        k += 1
        time.sleep(1)
        
try:
    GPIO.add_event_detect(mode1Btn, GPIO.FALLING, callback=mode1Btn_callback, bouncetime=300)
    GPIO.add_event_detect(mode2Btn, GPIO.FALLING, callback=mode2Btn_callback, bouncetime=300)
    
    print("go, ctrl+c")
    
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("end")
finally:
    GPIO.cleanup()