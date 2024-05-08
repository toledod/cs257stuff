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
               "she wants you fr", "whatever you were thinking about doing, dont", "don't do it lil bro", "tell zoey she a bitch for good luck",
              "sometimes wisdom comes in shutting up", "think of 3 things, you getting none of them", "buy a tequila bottle", "buy 2 tequila bottles",
              "google cute kittens rn", "shouldn't you be studying", "tell a freind your favorite song", "idk what to tell you lil bro", "try harder",
              "change your fit it's ass", "what the dog doin?"]
  num = random.randint(0, 18)
 
  message = "Welcome to Get A Fortune Cookie!"
  fortune1 = possibleF[num]
  return render_template("myhtml.html", someText = message, fortune = fortune1)

if __name__ == '__main__':
    my_port = 5000
    app.run(host='0.0.0.0', port = 5129) 
