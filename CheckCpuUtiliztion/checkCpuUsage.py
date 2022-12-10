import psutil

# 여기서 PID는 findProcessName에서 pid만 받아온 리스트
def checkCpuUsage(PID):
    for process in psutil.process_iter():
        for pid in PID:
            if str(process.pid) == str(pid):
                #cpu_percent에서 검사결과가 미미한 수준인경우 0.0으로 표시된다.
                print("CpuUsage of {0}({1}) : ".format(process.name(), process.pid) + str(process.cpu_percent(interval=1)))

checkCpuUsage(List)
