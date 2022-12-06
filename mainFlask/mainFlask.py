from flask import Flask, render_template
from datetime import datetime
import time
import psutil

from threading import Thread

app = Flask(__name__)

@app.route('/')
def home():
  global remained_time
  return render_template("time.html", time=remained_time,process_Name=process_name, Print_running=isrunning,
  Print_info=print_info, Process_NamePID=processNamePID)

def set_time():
    global remained_time
    
    while True:
        remained_time -= 1
        time.sleep(1)
        
        #if remained_time==0, kill process

    return

def checkProcessRunning(processname):
    for proc in psutil.process_iter():
        if processname.lower() in proc.name().lower():
            return True

def findProcessName(processName):
    listOfProcess=[]
    i=0
    for proc in psutil.process_iter():
        infoProcess=proc.as_dict(attrs=['name','pid'])

        if processName.lower() in infoProcess['name'].lower():
            listOfProcess.append(infoProcess)
            i+=1
    
    return listOfProcess

if __name__ == '__main__':
    remained_time = 300 # 관리자가 설정할 시간

    thread = Thread(target=set_time, daemon=True)
    thread.start()

    process_name='python'

    isRunning=checkProcessRunning(process_name)

    if isRunning:
        isrunning=True
        
        List=findProcessName(process_name)
        
        processNamePID=[]
        if len(List)>0:
            print("print_info=1")
            print_info=True
            
            for element in List:
                processNamePID.append(element['name'])
                processNamePID.append(element['pid'])

        else:
            print("print_info=0")
            print_info=False
        
    else:
        isrunning=0

    app.run(debug=True)
