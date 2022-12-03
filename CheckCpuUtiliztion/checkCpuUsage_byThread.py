import threading
import psutil

def checkCpuUsage(pid):
    for process in psutil.process_iter():
        if str(process.pid) == str(pid):
            print("CpuUsage of {0}({1}) : ".format(process.name(), process.pid)+ " " +str(process.cpu_percent(interval=1)))

# pid 갯수만큼 thread_cpu_i 에 할당.
for i in range(len(PID)):
    # pid마다 thread로 실행한다.
    thread = threading.Thread(target=checkCpuUsage, args=(PID[i],), daemon=True)
    thread.start()
