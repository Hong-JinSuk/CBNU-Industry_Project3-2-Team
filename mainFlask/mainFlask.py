from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
  global remained_time
  return render_template("time.html", time=remained_time)

def set_time():
    global remained_time
    
    while True:
        remained_time -= 1
        time.sleep(1)
        
        #if remained_time==0, kill process

    return
