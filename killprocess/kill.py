def killprocess(List, PID):
    for proc in psutil.process_iter():
        try:
            for i in PID:
                if List[i] == i:
                    parent_pid = List[i]  #PID
                    parent = psutil.Process(parent_pid)  #process 찾기
                    for child in parent.children(recursive=True):  #자식-부모 종료
                        child.kill()
                    parent.kill()

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):   #예외처리
            pass
