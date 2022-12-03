from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
  global remained_time
  return render_template("time.html", time=remained_time)

def test():
    global remained_time
