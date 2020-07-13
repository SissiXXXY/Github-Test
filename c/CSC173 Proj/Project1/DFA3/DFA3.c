#include <stdio.h>
#include <string.h>
#define TRUE 1
#define FALSE 0


typedef struct
{
    int current_status; //0: start, even 0s,  1: odd 0s,  2: final
    char input;
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

int transit(const DFA_Row* const dfa_tbl, const int dfa_row_cnt,
            const int current_status, const char input,
            int* const output, int* const next_status)
{
    for (int i = 0; i < dfa_row_cnt; i++)
    {
        DFA_Row* row = &DFA3_table[i];
        if (current_status == row->current_status && input == row->input)
        {
            //get the output and next status
            *next_status = row->next_status;
            *output = row->output;
            printf("(%d, %d) --> (%d,%d)\n", current_status, input, *next_status, *output);
            return TRUE; //successfully get identical row
        }
    }

    printf("ERROR: (%d, %d) no next status\n", current_status, input);
    return FALSE; //failed to get identical row
}

void main()
{
    const char* input_string = "10101010001110101010101";
    const int row_count = sizeof(DFA3_table) / sizeof(DFA_Row);
    int current = 0;
    int nextsta = 0;
    int output = 0;

    char* input_char_ptr = (char*)input_string;
    while (1)
    {
        const int ret = transit(DFA3_table, row_count, current, *input_char_ptr, &output, &nextsta);
        if (ret == FALSE)
        {
            printf("failed, unexpected internal error\n");
            return;
        }

        if (nextsta == 2)
        {
            printf("reach final status. output = %d\n", output);
            break;
        }

        if (*input_char_ptr == '\0')
        {
            printf("input string finished. current status=%d\n", nextsta);
            break;
        }

        input_char_ptr++;
        current = nextsta;
    }
}
