# Check if proecss is running
def processRunning(processName):
    print('>>>>>>> is running!!')

# Check if process is exist
def findProcessName(processName):
    print('>>>>>>> process name!!')



process_name='찾을려는 프로세스 이름'

isRunning=processRunning(process_name)

# Check isRunning
if isRunning:
    print(process_name + ' is running!!')
else:
    print(process_name + ' is no exist!!')

# if isRunning, print information of process
if isRunning:
    List=findProcessName(process_name)

    if 10>0:
        print('>>>>>> information of {}'.format(process_name))