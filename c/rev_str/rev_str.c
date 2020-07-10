#include<stdio.h>
#include<string.h>

int general_reverse(char* start, char* end) {
	if ((start != NULL) && (end != NULL)) {
		char* p = start;
		char temp = NULL;
		while (start < end) {
			temp = *start;
			*start = *end;
			*end = temp;
			start++;
			end--;
		}
		return 0;
	}
}
int inner_reverse(char* word) {
	if (word != NULL) {
		char* pword = word;
		char* begin = word;
		char* last = word;
		while (*last != "\0") {
			last++;
			if (*last == " ") {
				break;
			}
			general_reverse(begin,(last-1))
			
		}

	}
}

