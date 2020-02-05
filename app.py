from flask import Flask
import Rpi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)
gpio.setup(11, gpio.OUT)
gpio.setup(13, gpio.OUT)

app = Flask(__name__)

@app.route('/')
def index():
    return 'This is the smart curtain url'

@app.route('/up')
def up():
    time_param = request.args.get('time')
    time_param = int(time_param) if time_param else 5
    print(f"raising curtain {time_param}")
    gpio.output(13,True)
    gpio.output(11,True)
    time.sleep(time_param)
    gpio.output(11,False)


@app.route('/down')
def down():
    time_param = request.args.get('time')
    time_param = int(time_param) if time_param else 5
    print(f"lowering curtain {time_param}")
    gpio.output(13,False)
    gpio.output(11,True)
    time.sleep(time_param)
    gpio.output(11,False)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')