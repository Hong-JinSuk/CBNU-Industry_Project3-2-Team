import threading
import psutil

def checkCpuUsage(pid):
    for process in psutil.process_iter():
        if str(process.pid) == str(pid):
            print("CpuUsage of {0}({1}) : ".format(process.name(), process.pid)+ " " +str(process.cpu_percent(interval=1)))

# pid 갯수만큼 thread_cpu_i 에 할당.
for i in range(len(PID)):
    globals()["thread_cpu_{}".format(i+1)] = threading.Thread(target=checkCpuUsage, args=(PID[i],), daemon=True)

thread_cpu_1.start()
thread_cpu_2.start()
thread_cpu_3.start()
thread_cpu_4.start()
thread_cpu_5.start()
