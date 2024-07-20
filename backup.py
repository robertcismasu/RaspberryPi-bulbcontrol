from flask import Flask, render_template
from signal import signal, SIGTERM ,SIGHUP, pause
from rpi_lcd import LCD
import datetime
import RPi.GPIO as GPIO
from time import sleep

lcd = LCD()
app = Flask(__name__)

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD) # 
GPIO.setup(11, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(13, GPIO.OUT, initial=GPIO.HIGH)

templateData = {
      'title' : 'Bulb Light Control',
      'ModeStatuts' : 'OFF'
      }

def safe_exit(signum,frame):
    exit(1)
signal(SIGTERM, safe_exit)
signal(SIGHUP, safe_exit)


@app.route('/')
def index():
    return render_template('index.html', **templateData)

@app.route("/AutoMode/on")
def AutoActionON():
		lcd.text("MODE: AUTO",1)
		GPIO.output(13, GPIO.HIGH)
		GPIO.output(11, GPIO.LOW)     
		templateData['ModeStatuts'] = 'AUTO'
		return render_template('index.html', **templateData)	

@app.route("/AutoMode/off")
def AutoActionOFF():
    GPIO.output(11, GPIO.HIGH)
    templateData['ModeStatuts'] = 'AUTO'
    return render_template('index.html', **templateData)




@app.route("/ManualMode/on")
def ManualActionON():
	lcd.clear()
	lcd.text("MODE: MANUAL",1)
	GPIO.output(11, GPIO.HIGH)
	GPIO.output(13, GPIO.LOW)
	templateData['ModeStatuts'] = 'MANUAL'
	return render_template('index.html', **templateData)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)