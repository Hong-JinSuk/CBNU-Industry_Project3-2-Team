#include<Windows.h>
#include<iostream>
#include<stdio.h>
//CreateToolhelp32Snapshot(), Process32First(), Process32Next() 사용하기위한 라이브러리
#include<TlHelp32.h>

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
            cout << pe32.szExeFile << "     " << pe32.th32ProcessID << endl;

        }
    }
    else {
        printf("CHECK --------------");
    }

    return 0;

}