#include <stdio.h> 
#include <string.h>
#define TRUE 1
#define FALSE 0


typedef struct {
	int current_status;//0: start, even 0s,  1: odd 0s,  2: final
	char input;
	int output; // -1: void,  0: false,  1: true
	int next_status;
}DFA_Row;

DFA_Row DFA3_table[] = {
	{0, '0', -1, 1}, //
	{0, '1', -1, 0},
	{0, '\0', 1, 2},
	{1, '0', -1, 0},
	{1, '1', -1, 1},
	{1, '\0', 0, 2}

};

int transit(int current_status, char input, int* output, int* next_status, int row)
{	
	int result = -1;
	DFA_Row* dfar=DFA3_table;
	current_status = 0;
	for (int i = 0; i < row; i++) {
		dfar = &DFA3_table[i];
		if (current_status == dfar->current_status) {//first element match
			if (input== dfar->input) {//second element match
				//get the output and next status
				*next_status = dfar->next_status;
				*output = dfar->output;
				return TRUE;//successfully get identical row

				if (*next_status == 2) {
					break;//final status
				}

			}
		}
	}
	return FALSE;//failed to get identical row

}



void main() {
	char* input_string = "01010001010100101110100101";
	int row_count = sizeof(DFA3_table) / sizeof(DFA_Row);
	int current = 0;
	int nextsta = 0;
	int output = -1;
	int* outp = &output;
	int* next = &nextsta;

	for (int i = 0; i < (int)strlen(input_string); i++) {
		current = nextsta;
		char inp = input_string[i];
		transit(current, inp, outp, next, row_count);
	}
	if (*outp == 1) {
		printf("TRUE");
	}
	else if (*outp == 0) {
		printf("FALSE");
	}
	else {
		printf("FAILED");
	}
}