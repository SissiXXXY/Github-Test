#include<stdio.h>
#include<string.h>


typedef struct
{
	int current_status; //0: start, even 0s,  1: odd 0s,  2: final
	int check_result;
	//int (*funcptr)(char);
	//char input;
	int output; // -1: void,  0: false,  1: true
	int next_status;
} DFA_Row;

DFA_Row DFA3_table[] = {
	{0, '0', -1, 1}, //
	{0, '1', -1, 0},
	{0, '\0', 1, 2},
	{1, '0', -1, 0},
	{1, '1', -1, 1},
	{1, '\0', 0, 2}

};

int check(char in, char except) {
	if (in == except) {
		return 1;
	}
	else {
		return 0;
	}
}

int NFA2(char* in) {
	int current_status = 0; //0: none; 1: c; 2: co; 3: cod; 4:code;
	char c = 'c';
	char o = 'o';
	char d = 'd';
	char e = 'e';
	for (int i = 0; i <(int)strlen(in); i++) {
		char this = *(in + i);
		
		if (this==c) {
			current_status = 1;
			if (*(in + i + 1) == o) {
				current_status = 2;
				if (*(in + i + 2)==d){
					current_status = 3;
					if (*(in + i + 3) ==e) {
						current_status = 4;
						return 1;
					}
					else { //not code
						current_status = 0;
						continue;
					}
				}
				else { //not cod
					current_status = 0;
					continue;
				}
			}
			else {//not co
				current_status = 0;
				continue;
			}
		}
		else {//not c
			current_status = 0;
		}
	}
	return 0;
}

void main() {
	printf("Please enter your test('exit' to quit): \n");
	char typein[10000];
	scanf_s("%9999s", &typein, 10000);
	if (strcmp(typein, "exit") == 0) {
		return;
	}
	else if (NFA2(typein) == 1) {
		printf("The input %s result: TRUE", typein);
	}
	else if (NFA2(typein) == 0) {
		printf("The input %s result: FALSE", typein);
	}
	else {
		printf("FAILED\n");
	}
}