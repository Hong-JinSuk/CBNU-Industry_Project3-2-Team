import psutil

# 여기서 PID는 findProcessName에서 pid만 받아온 리스트
def checkCpuUsage(PID):
    for process in psutil.process_iter():
        for pid in PID:
            if str(process.pid) == str(pid):
                print("CpuUsage of {} : ".format(process.name()) + str(process.cpu_percent(interval=1)))

checkCpuUsage(List)
