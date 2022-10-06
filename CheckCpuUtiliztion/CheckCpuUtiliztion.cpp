#include <iostream>
#include <Pdh.h>

using namespace std;

float getCpu() {

}

void printCpu() {
	while (true) {

		cout << "Cpu Usage : " << getCpu() << endl;
		Sleep(1000);

		/*if (shutdownCom) {
			inputTime();
			break;
		}*/
	}
}

int main() {

	printCpu();

	return 0;
}