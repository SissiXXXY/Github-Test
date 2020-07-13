#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define TRUE 1
#define FALSE 0

int DFA1(char* in) {
		if (strcmp(in, "csc173") == 0) {
			return TRUE;
		}
		return FALSE;
}




void main() {
	printf("Please enter your test('exit' to quit): \n");
	char typein[7];
	scanf_s("%6s", &typein,7);
	DFA1(typein);
	if (strcmp(typein, "exit") == 0) {
		return;
	}
	else if (DFA1(typein) == FALSE) {
		printf("The input %s result: FALSE", typein);
	}
	else if (DFA1(typein) == TRUE) {
		printf("The input %s result: TRUE", typein);
	}
	else {
		printf("FAILED");
	}

}

