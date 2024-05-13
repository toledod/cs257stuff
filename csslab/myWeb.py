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
  possibleF = [
    "A dream you dream alone is only a dream. A dream you dream together is reality.",
    "A friend asks only for your time, not your money.",
    "A golden egg of opportunity falls into your lap this month.",
    "A good friendship is often more important than a passionate romance.",
    "A hunch is creativity trying to tell you something.",
    "A lifetime of happiness lies ahead of you.",
    "A light heart carries you through all the hard times.",
    "A new perspective will come with the new year.",
    "A person is never to (sic) old to learn.",
    "A pleasant surprise is waiting for you.",
    "A smile is your personal welcome mat.",
    "A smooth long journey! Great expectations.",
    "A soft voice may be awfully persuasive.",
    "A truly rich life contains love and art in abundance.",
    "Accept something that you cannot change, and you will feel better.",
    "Adventure can be real happiness.",
    "Advice, when most needed, is least heeded.",
    "All will go well with your new project.",
    "All your hard work will soon pay off.",
    "Allow compassion to guide your decisions.",
    "An acquaintance of the past will affect you in the near future.",
    "An exciting opportunity lies ahead.",
    "An inch of time is an inch of gold.",
    "Any decision you have to make tomorrow is a good decision.",
    "At the touch of love, everyone becomes a poet.",
    "you will slip on a bannana",
]
  num = random.randint(0, len(possibleF) - 1)
 
  message = "Welcome to Get A Fortune Cookie!"
  fortune1 = possibleF[num]
  return render_template("myhtml.html", someText = message, fortune = fortune1)

if __name__ == '__main__':
    my_port = 5000
    app.run(host='0.0.0.0', port = 5129) 
