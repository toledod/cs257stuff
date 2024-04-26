from flask import Flask
from flask import render_template
import random

app = Flask(__name__)

@app.route('/')
def welcomeScreen():
  return render_template("myIndex.html")

@app.route('/name)
def getName();
  randomNum = random.randint(0, 19)
  nameList = ["Gelad", "Howard", "Jose", "Veronica", "Frank", "Deven", "Pooh Shiesty", "Willian", "Craig", "Josie",
              "Melanie", "Mellisa", "Bianca", "Steven", "Angel's bitch ass", "Allen", "Sharon", "Ben", "Kevin", "Alex"]
  nameChosen = nameList[randomNum]
  return render_template("gotName.html", name = nameChosen)
  
