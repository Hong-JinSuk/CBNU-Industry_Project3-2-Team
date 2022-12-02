import threading
import psutil

def checkCpuUsage(pid):
    for process in psutil.process_iter():
        if str(process.pid) == str(pid):
            print("CpuUsage of {0}({1}) : ".format(process.name(), process.pid)+ " " +str(process.cpu_percent(interval=1)))
