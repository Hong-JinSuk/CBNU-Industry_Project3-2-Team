def killprocess(PID):
    for proc in psutil.process_iter():
        try:        
            # 프로세스 이름, PID값 가져오기
            processName = proc.name()
            processID = proc.pid

            for i in PID:    #PID 리스트에 있는 모든 프로세스 종료를 위한 반복
                if processID == i:
                    parent_pid = processID
                    parent = psutil.Process(parent_pid)
                    for child in parent.children(recursive=True):  #자식-부모 종료
                        child.kill()
                    parent.kill()

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):   #예외처리
            pass
