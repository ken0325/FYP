from flask import Flask, render_template, request
import RPi.GPIO as GPIO

app = Flask(__name__)

# Setup GPIO
LED_PIN = 32
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_PIN, GPIO.OUT)

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/<action>')
# def action(action):
#     if action == "on":
#         GPIO.output(LED_PIN, True)
#     elif action == "off":
#         GPIO.output(LED_PIN, False)
#     return render_template('index.html')

@app.route('/LED/<action>')
def action(action):
    if action == "on":
        GPIO.output(LED_PIN, True)
    elif action == "off":
        GPIO.output(LED_PIN, False)
    return render_template('index.html')

@app.route('/cleanup')
def cleanup():
    GPIO.cleanup()
    return "GPIO cleaned up!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)