#include<stdio.h>
#include <math.h>
#include <time.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>

typedef struct
{
	char* pdata;
	int capacity;
	int size;
} list_t;

int list_init(list_t* plist, int capacity)
{
	plist->pdata = (char*)malloc(sizeof(plist->pdata[0]) * capacity);
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

void list_print(list_t* plist)
{
	for (int i = plist->size-1; i >= 0; i--)
	{	
		if (i == plist ->size - 1 && plist->pdata[i] == 0) {
			continue;
		}
		printf("%d", plist->pdata[i]);
	}
	printf("\n");
}

int list_add(list_t* plist1, list_t* plist2, list_t* pnext)
{
	int carry = 0;

	int diff = plist1->size - plist2->size;
	//fill up the shorter list with zeros
	if (diff > 0) {
		for (int i = 0; i < diff; i++) {
			list_append(plist2, 0);
		}
	}
	if (diff < 0) {
		for (int i = 0; i < -diff; i++) {
			list_append(plist1, 0);
		}
	}


	int i = 0;
	while (1)
	{
		if (i >= plist1->size)//0 base
		{//break when out of range
			break;
		}
		int s = plist1->pdata[i] + plist2->pdata[i];
		if (carry == 1)
		{//has carry
			s += 1;//add carry
			carry = 0;//clear carry
		}
		if (s > 9)
		{
			carry = 1;
			s = s - 10;
		}
		list_append(pnext, s);//store backwards
		i++;
	}
	if (carry > 0)
	{
		list_append(pnext, 1); //if has carry after the last digit,append 1
	}

	return 1;
}


int main(void)
{
	list_t fibo[1000];//store all the pointers referring to the elements in fibo
	list_t* pfibo = fibo;//the pointer of the whole array
	list_t* pfirst = fibo;
	list_t* psecond = pfirst + 1;
	if (list_init(pfirst, 50000) == 0)
	{
		printf("first init failed\n");
		return -1;
	}

	if (list_init(psecond, 50000) == 0)
	{
		printf("second init failed\n");
		return -1;
	}

	const clock_t start = clock();
	list_append(pfirst, 1);
	list_append(psecond, 1);

	for (int i = 2; i < 1000; i++)
	{
		list_init(pfibo + i, 50000);
		list_add(pfibo + i - 2, pfibo + i - 1, pfibo + i);
	}
	for (int i = 0; i < 1000; i++)
	{
		list_print(pfibo + i);
		//printf("%d", pfibo[i]);
	}
	const clock_t end = clock();
	printf("%.3f seconds", (end - start) / (double)CLOCKS_PER_SEC);

	for (int i = 0; i < 1000; i++)
	{
		list_destroy(pfibo + i);
	}

	return 0;
}

