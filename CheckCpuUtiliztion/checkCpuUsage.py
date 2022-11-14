import psutil

List=[]
for i in psutil.process_iter():
    List.append(i)

def checkCpuUsage(List):
    for process in List:
        if str(process.name()) == "python3.9.exe":
            print("CpuUsage of {} : ".format(process.name()) + str(process.cpu_percent()))

checkCpuUsage(List)