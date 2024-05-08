from flask import Flask
from flask import render_template
import random


app = Flask(__name__)

@app.route('/')
def welcome():
  message = "Welcome to Get A Fortune Cookie!"
  fortunePlace = "click the cookie!"
  return render_template("myhtml.html", someText = message, fortune = fortunePlace)
  
@app.route('/fortune')
def cookieClick():
  possibleF = ["you getting mad bitches", "you gonna die tmr", "good luck...", "you thought you were gonna get something good?",
               "she wants you fr", "whatever you were thinking about doing, dont", "don't do it lil bro", "tell zoey she a bitch for good luck"]
  num = random.randint(0, 7)
  possibleF2 = ["tell zoey she a bitch for good luck", "if you see zoey today, you failing your next test", "call zoey, if she answers: good luck for 7 days",
                "if zoey goes to HCI tmr, everyone gets a cookie"]
  message = "Welcome to Get A Fortune Cookie!"
  fortune1 = possibleF[num]
  return render_template("myhtml.html", someText = message, fortune = fortune1)

if __name__ == '__main__':
    my_port = 5000
    app.run(host='0.0.0.0', port = 5129) 
