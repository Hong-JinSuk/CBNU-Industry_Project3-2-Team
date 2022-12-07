import psutil
 
for proc in psutil.process_iter():
    try: 
        if processName == "notepad.exe":
            parent_pid = processID  #PID
            parent = psutil.Process(parent_pid) # PID 찾기
            for child in parent.children(recursive=True):  #자식-부모 종료
                child.kill()
            parent.kill()
 
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):   #예외처리
        pass
