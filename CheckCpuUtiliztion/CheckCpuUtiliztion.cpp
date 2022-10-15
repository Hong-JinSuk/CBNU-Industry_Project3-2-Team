#pragma comment(lib, "pdh.lib")
#include <iostream>
#include <Pdh.h>

using namespace std;

// get current cpu
static PDH_HQUERY cpuQuery;
static PDH_HCOUNTER cpuTotal;


void init() {
	PdhOpenQuery(NULL, NULL, &cpuQuery);
	PdhAddCounter(cpuQuery, L"\\Processor(_Total)\\% Processor Time", NULL, &cpuTotal);
	PdhCollectQueryData(cpuQuery);
}

float getCpuUsage() {
	
	// operator definition
	PDH_FMT_COUNTERVALUE counterVal;
	
	// get cpuQuery and find value
	PdhCollectQueryData(cpuQuery);
	PdhGetFormattedCounterValue(cpuTotal, PDH_FMT_DOUBLE, NULL, &counterVal);
	return counterVal.doubleValue;
}

void printCpu() {
	while (true) {

		cout << "Cpu Usage : " << getCpuUsage() << endl;
		Sleep(1000);

		/*if (shutdownCom) {
			inputTime();
			break;
		}*/
	}
}

int main() {
	
	init();

	printCpu();

	return 0;
}
