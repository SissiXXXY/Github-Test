#include<stdio.h>
#include <math.h>
#include <time.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>

typedef struct
{
	int* pdata;
	int capacity;
	int size;
} list_t;

int list_init(list_t* plist, int capacity)
{
	plist->pdata = (int*)malloc(sizeof(int) * capacity);
	plist->capacity = capacity;
	plist->size = 0; 
	return plist->pdata != NULL;
}

void list_destroy(list_t* plist)
{
	free(plist->pdata);
}

int list_append(list_t* plist, int val)
{
	if (plist->size == plist->capacity) 
	{
		int new_size = 2 * plist->size;
		void* pnewdata = realloc(plist->pdata, sizeof(int) * new_size);
		if (pnewdata == NULL)
		{
			printf("running out of space\n");
			return -1;
		}
		else 
		{
			plist->capacity = new_size;
			plist->pdata = pnewdata;
		}
	}

	plist->pdata[plist->size] = val;
	plist->size++;
	return 0;
}

list_t* list_add(list_t* plist1, list_t* plist2)
{
	list_t next;
	list_t pnext = &next;
	if (list_init(pnext, 50000) == 0)
	{
		printf("next init failed\n");
		return -1;
	}

	int carry = 0;
	
	int diff = plist1->size - plist2->size;
	//fill up the shorter list with zeros
	if (diff > 0) {
			for (int i = 0; i < diff; i++) {
				list_append(plist2, 0);
			}
		}
	if (diff < 0) {
			for (int i = 0; i < diff; i++) {
				list_append(plist1, 0);
			}
		}
	
	
	int i = 0;
	while true
	{
		if (i > plist1->size) 
		{//break when out of range
			break;
		}
		int s=plist1[i] + plist2[i];
		if (carry = 1) 
		{//has carry
			s += 1;//add carry
			carry = 0;//clear carry
		}
		if (s > 9) 
		{
			carry = 1;
			s = s - 10;
		}
		list_append(, s);//store backwards
		i++;
	}
	if (carry > 0) 
	{
		list_append(pnext, 1); //if has carry after the last digit,append 1
	}
	
	return pnext;
}


int main(void)
{
	list_t fibo;//store all the pointers referring to the elements in fibo
	list_t* pfibo = &fibo;
	list_t first;//store the former value
	list_t second;//store the latter value
	if (list_init(&first, 50000) == 0)
	{
		printf("first init failed\n");
		return -1;
	}

	if (list_init(&second, 50000) == 0) 
	{
		printf("second init failed\n");
		return -1;
	}

	if (list_init(&pfibo, 1000) == 0)
	{
		printf("pfibo init failed\n");
		return -1;
	}
	const clock_t start = clock();
	for (...)
	{
		list_append(pfibo, pnext)
	}
	const clock_t end = clock();
	printf("%.3f seconds", (end - start) / (double)CLOCKS_PER_SEC);

	list_destroy(&primeList);

	return 0;
}

