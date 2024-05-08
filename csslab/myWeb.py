from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def welcome():
  message = "Welcome to Get A Fortune Cookie!"
  return render_template("myhtml.html", someText = message)

if __name__ == '__main__':
    my_port = 5000
    app.run(host='0.0.0.0', port = 5129) 
