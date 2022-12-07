def killprocess(PID):
    for proc in psutil.process_iter():
        try:
            # 프로세스 이름, PID 값 가져오기
            processName = proc.name()
            processID = proc.pid
            print(processName , ' - ', processID)

            for i in PID:
                if processID == i:
                    parent_pid = processID  #PID
                    parent = psutil.Process(parent_pid)  #process 찾기
                    for child in parent.children(recursive=True):  #자식-부모 종료
                        child.kill()
                    parent.kill()

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):   #예외처리
            pass
