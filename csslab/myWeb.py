from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def welcome():
  message = "Welcome to Get A Fortune Cookie!"
  return render_template("myhtml.html", someText = message)
