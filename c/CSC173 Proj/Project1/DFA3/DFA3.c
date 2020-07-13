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

int row_init(DFA_Row* prow, int current_status, char input, int output, int next_status)
{
	malloc(sizeof(DFA_Row));
	prow->current_status = current_status;
	prow->input = input;
	prow->output = output;
	return prow != NULL;
}

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
			if (strcmp(input, dfar->input) == 0) {//second element match
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
	DFA_Row first;
	row_init(&first, 0, '0', -1, 1);
	DFA_Row second;
	row_init(&second, 0, '1', -1, 0);
	DFA_Row third;
	row_init(&third, 0, '\0', 1, 2);
	DFA_Row fourth;
	row_init(&fourth, 1, '0', -1, 0);
	DFA_Row fifth;
	row_init(&fifth, 1, '1', -1, 1);
	DFA_Row sixth;
	row_init(&sixth, 1, '\0', 0, 2);
	int current = 0;
	int nextsta = 0;
	int output = -1;
	int* outp = &output;
	int* next = &nextsta;
	/// <summary>
	/// initialize the table here?
	/// </summary>
	for (int i = 0; i < (int)strlen(input_string); i++) {
		current = nextsta;
		char inp = input_string[i];
		transit(current, inp, outp, next, row_count);
	}
}