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
    plist->pdata = malloc(sizeof(plist->pdata[0]) * capacity);
    plist->capacity = capacity;
    plist->size = 0;
    return plist->pdata != NULL;
}

void list_destroy(list_t* plist)
{
    free(plist->pdata);
}

int list_append(list_t* plist, char val)
{
    if (plist->size == plist->capacity)
    {
        const int new_size = 2 * plist->size;
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
    for (int i = plist->size - 1; i >= 0; i--)
    {
        const char val = plist->pdata[i];
        if (i == plist->size - 1 && val == 0)
        {
            continue;
        }
        printf("%d", val);
    }
    printf("\n");
}

int list_add(list_t* plist1, list_t* plist2, list_t* pnext)
{
    // fill up the shorter list with zeros
    const int diff = plist1->size - plist2->size;
    if (diff > 0)
    {
        for (int i = 0; i < diff; i++)
        {
            list_append(plist2, 0);
        }
    }
    else if (diff < 0)
    {
        for (int i = 0; i < -diff; i++)
        {
            list_append(plist1, 0);
        }
    }

    // add two list
    char carry = 0;
    for (int i = 0; i < plist1->size; i++)
    {
        char s = plist1->pdata[i] + plist2->pdata[i];
        if (carry == 1)
        {
            //has carry
            s += 1; //add carry
            carry = 0; //clear carry
        }
        if (s > 9)
        {
            carry = 1;
            s = s - 10;
        }
        list_append(pnext, s); //store backwards
    }

    if (carry > 0)
    {
        list_append(pnext, 1); //if has carry after the last digit,append 1
    }

    return 1;
}


int main(void)
{
#define CNT 2000

    list_t fibo[CNT]; //store all the pointers referring to the elements in fibo
    for (int i = 0; i < CNT; i++)
    {
        if (list_init(&fibo[i], 50000) == 0)
        {
            printf("init failed\n");
            return -1;
        }
    }

    const clock_t start = clock();

    list_append(&fibo[0], 1);
    list_append(&fibo[1], 1);

    for (int i = 2; i < CNT; i++)
    {
        list_add(&fibo[i - 2], &fibo[i - 1], &fibo[i]);
    }
    for (int i = CNT - 100; i < CNT; i++)
    {
        list_print(&fibo[i]);
    }
    const clock_t end = clock();
    printf("%.3f seconds", (end - start) / (double)CLOCKS_PER_SEC);

    for (int i = 0; i < CNT; i++)
    {
        list_destroy(&fibo[i]);
    }

    return 0;
}
