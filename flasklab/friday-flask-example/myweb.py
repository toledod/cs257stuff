from flask import Flask
from flask import render_template
import random

app = Flask(__name__)

@app.route('/')
def welcomeScreen():
  return render_template("myIndex.html")
  
