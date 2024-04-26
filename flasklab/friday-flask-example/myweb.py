from flask import Flask
from flask import render_template
import random

app = Flask(__name__)

@app.route('/')
def getName():
  conn = psycopg2.connect(
    host="localhost",
    port=5432,   
    database="toledod",
    user="toledod",
    password="mask777glass")
  
  cur = conn.cursor()
  
  sql = "SELECT * FROM usstatepop WHERE code = %s;"
