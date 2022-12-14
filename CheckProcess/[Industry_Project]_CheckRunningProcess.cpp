#include<Windows.h>
#include<iostream>
#include<stdio.h>
//CreateToolhelp32Snapshot(), Process32First(), Process32Next() 사용하기위한 라이브러리
#include<TlHelp32.h>
// for change WCHAR to Char
#include<comdef.h>
#include<stdlib.h>

using namespace std;

int main(void) {

    HANDLE hProcess = NULL;

    // 프로세스의 정보를 저장할 구조체.
    PROCESSENTRY32 pe32 = { 0 };

    // 모든 프로세스를 받아온다.
    hProcess = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0);

    // 구조체의 크기를 정해줌.
    pe32.dwSize = sizeof(PROCESSENTRY32);

    cout << "System Process Name" << "          " << "PID" << endl;

    // 구조체에서 정보를 받아오면
    if (Process32First(hProcess, &pe32)) {

        // 다음 프로세스의 정보도 받아온다.
        while (Process32Next(hProcess, &pe32)) {

            // szExeFile : 프로세스의 이름, th32ProcessID : PID
            
            _bstr_t PN(pe32.szExeFile);
            const char* processName = PN;
            
            //WCHAR은 cmd에 정상적으로 출력이 안되서 char형으로 바꾸고 출력을 해줘야한다.
            //cout << processName << "     " << pe32.th32ProcessID << endl;
            
            if(!strcmp(processName, "processName")){
                
                string process_name;
                process_name = (string)processName;
                
                cout << "[      System Process Name      ]" << "  " << "[ PID ]" << endl;
                
                // 그냥 볼때, 편하게 보라고,,,
                double sizeOfProcessName = process_name.length();
                double temp = (sizeOfProcessName - sizeof("[      System Process Name      ]")) / 2;
                
                
                for (int i = 0; i < abs(temp); i++) {
                    cout << " ";
                }
                cout << processName;
                for (int i = 0; i < abs(temp); i++) {
                    cout << " ";
                }
                cout << "  ";
                cout << pe32.th32ProcessID << endl;
            }

        }
    }
    else {
        cout << "-------------Error or End part -------------" << endl;
    }

    return 0;

}
