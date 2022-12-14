from flask import Flask, render_template
from datetime import datetime
import time
import psutil

from threading import Thread

app = Flask(__name__)

@app.route('/')
def home():
  global remained_time
  global list_cpu_percent
  global print_info

  return render_template("time.html", time=remained_time,process_Name=process_name, Print_running=isrunning,
  Print_info=print_info, Process_NamePID=processNamePID)

def set_time(PID):
    global remained_time
    global list_cpu_percent
    
    while True:
        remained_time -= 1
        time.sleep(1)
        
        if remained_time == 0 :
            killprocess(PID)
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

def killprocess(PID):
    for proc in psutil.process_iter():
        try:
            # 프로세스 이름, PID 값 가져오기
            processName = proc.name()
            processID = proc.pid

            for i in PID:
                if processID == i:
                    parent_pid = processID  #PID
                    parent = psutil.Process(parent_pid)  #process 찾기
                    for child in parent.children(recursive=True):  #자식-부모 종료
                        child.kill()
                    parent.kill()

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):   #예외처리
            pass

def checkCpuUsage_thread(pid):
    global list_cpu_percent
    while True:
        for process in psutil.process_iter():
            if str(process.pid) == str(pid):
                Cpu_Per=process.cpu_percent(interval=10)
                list_cpu_percent.append(Cpu_Per)
                #print("CpuUsage of {0}({1}) : ".format(process.name(), process.pid)+ " " +str(Cpu_Per))
        time.sleep(10)
        list_cpu_percent.clear()
        
def checkMemoryUsage(PID):
    while True:
        for pid in PID:
            #print("--"*30)
            #print(pid)
            # current process RAM usage
            total_memory = psutil.virtual_memory()
            print(total_memory[2]) #psutil.virtual_memory()는 3번째 원소에 메모리 사용률을 반환함.
            
            # pid별 메모리 사용률을 받아와야함.
            current_process = psutil.Process(pid)
            current_process_memory_usage_as_GB = current_process.memory_info()[0] / 3.**20
            print(f"Current memory GB   : {current_process_memory_usage_as_GB: 9.3f} GB")
        time.sleep(10)
        
if __name__ == '__main__':
    
    global remained_time
    remained_time = 10
    
    while True:
        
        global print_info
    
        process_name='python'
        print_info=0
        processNamePID=[]
        PID=[]

        isRunning=checkProcessRunning(process_name)

        if isRunning:
            isrunning=True

            List=findProcessName(process_name)

            if len(List)>0:
                print("print_info=1")
                print_info=True

                for element in List:
                    processNamePID.append(str(element['pid']) + " " + str(element['name']))

            else:
                print("print_info=0")
                print_info=False
                
            for element in List:
                PID.append(element['pid'])

            thread = Thread(target=set_time, args=(PID,), daemon=True)
            thread.start()

            list_cpu_percent=[]
            for i in range(len(PID)):
                    thread = Thread(target=checkCpuUsage_thread, args=(PID[i],), daemon=True)
                    thread.start()

            thread = Thread(target=checkMemoryUsage, args=(PID,), daemon=True)
            thread.start()

        else:
            isrunning=0

        app.run(debug=True)
        
        time.sleep(1)
