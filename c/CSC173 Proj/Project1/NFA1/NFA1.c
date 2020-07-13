#include<stdio.h>
#include<string.h>
//accepting strings ending in 'code'

int NFA1(char* in){
	if (strlen(in) < 4) {
		return 0;
	}
	else {
		char* last = in + (strlen(in) - 4);
		if (strcmp(last, "code") == 0) {//last 4 char is code
			return 1;
		}
		else {
			return 0;
		}
	}
}

void main() {
	printf("Please enter your test('exit' to quit): \n");
	char typein[10000];
	scanf_s("%9999s", &typein, 10000);
	if (strcmp(typein, "exit") == 0) {
		return;
	}
	else if (NFA1(typein) == 1) {
		printf("The input %s result: TRUE", typein);
	}
	else if (NFA1(typein) == 0) {
		printf("The input %s result: FALSE", typein);
	}
	else {
		printf("FAILED\n");
	}
	
}