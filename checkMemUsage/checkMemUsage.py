import psutil

# PID : 실행중인 프로세스의 PID 리스트
def checkMemoryUsage(PID):
    for pid in PID:
        print("--"*30)
        # current process RAM usage
        # 여기에 psutil을 이용해서 MemUsage를 받아오는 소스 작성
