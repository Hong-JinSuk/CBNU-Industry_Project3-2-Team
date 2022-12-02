import threading
import psutil

def checkCpuUsage(pid):
    for process in psutil.process_iter():
        if str(process.pid) == str(pid):
            print("CpuUsage of {0}({1}) : ".format(process.name(), process.pid)+ " " +str(process.cpu_percent(interval=1)))

for i in range(len(PID)):
    # 할당해줄 thread을 pid 갯수만큼 선언
    # thread를 이용한 병렬처리
    globals()["thread_cpu_{}".format(i+1)]
