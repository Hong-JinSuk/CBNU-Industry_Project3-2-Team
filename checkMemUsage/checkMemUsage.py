import psutil

# PID : 실행중인 프로세스의 PID 리스트
def checkMemoryUsage(PID):
    for pid in PID:
        print("--"*30)
        # current process RAM usage
        total_memory = psutil.virtual_memory()
        print(total_memory[2]) #psutil.virtual_memory()는 3번째 원소에 메모리 사용률을 반환함.
        # pid별 메모리 사용률을 받아와야함.
