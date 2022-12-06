import psutil

# Check if proecss is running
def checkProcessRunning(processName):
    print('>>>>>>>> isRunning Checking...')
    # get all the running process
    for proc in psutil.process_iter():
        if processName.lower() in proc.name().lower():
            return True
    print(">>>>>>>> complete!!")


# Check if process is exist
def findProcessName(processName):
    listOfProcess=[]
    i=0
    print('>>>>>>>> isExist Checking...')
    for proc in psutil.process_iter():
        infoProcess=proc.as_dict(attrs=['name','pid'])

        if processName.lower() in infoProcess['name'].lower():
            listOfProcess.append(infoProcess)
            i+=1
    
    print("키워드를 포함하는 실행중인 프로세스가 {}개 있습니다. ".format(i))
    return listOfProcess


process_name='python'

isRunning=checkProcessRunning(process_name)

# Check isRunning
if isRunning:
    print(process_name + ' is running!!')
else:
    print(process_name + ' is no exist!!')

# if isRunning, print information of process
if isRunning:
    List=findProcessName(process_name)

    # if process is exist in list
    if len(List)>0:
        print('>>>>>>>> information of {}'.format(process_name))
        for element in List:
            processName = element['name']
            processPID = element['pid']
            print(processPID, processName)
    else:
        print('키워드를 포함하는 실행중인 프로세스가 없습니다.')

    print('>>>>>>>> 검사 종료')
