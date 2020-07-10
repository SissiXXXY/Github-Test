#include <stdio.h>
#include <string.h>
#define TRUE 1
#define FALSE 0

int DFA2(char* in) {
	if (strlen(in) < 3) {
		return FALSE;
	}
	else {
		if (strncmp(in, "cat", 3)==0) {
			return TRUE;
		}
		else {
			return FALSE;
		}
	}
	
}

void main() {
	printf("Please keep the length under 20 letters\n");
	printf("Please enter your test('exit' to quit): \n");
	char typein[21];
	scanf_s("%20s", &typein, 21);
	DFA2(typein);
	if (strcmp(typein, "exit") == 0) {
		return;
	}
	if (DFA2(typein) == FALSE) {
		printf("The input %s result: FALSE", typein);
	}
	else {
		printf("The input %s result: TRUE", typein);
	}
}