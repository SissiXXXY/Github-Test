#include <stdio.h>
#include <math.h>
#include <time.h>
#include <stdint.h>

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
    printf("successfully create a list");
}

void list_destroy(list_t* plist)
{
    free(plist->pdata);
}

int list_append(list_t* plist, int val)
{
    if (plist->size == plist->capacity) {
        ensure_capacity(plist);
    }
    else {
        plist->pdata[plist->size] = val;
        plist->size++;
    }
    return 0;
}

int ensure_capacity(list_t* plist) 
{
    if (plist->size >= plist->capacity) {
        ()
    }
}
int is_prime(list_t* plist, int num)
{
    const int threshold = (int)sqrt(num);
    for (int i = 0; i < plist->size; i++)
    {
        const int b = plist->pdata[i];
        if (num % b == 0)
        {
            return 0;
        }
        if (b > threshold)
        {
            break;
        }
    }
    return 1;
}

void getprime(list_t* plist)
{
    list_append(plist, 2);
    for (int num = 3; num < 100000; num++)
    {
        if (is_prime(plist, num) != 0)
        {
            list_append(plist, num);
            printf("%d\n", num);
        }
    }
}

int main(void)
{
    list_t primeList;
    if (list_init(&primeList, 100) == 0)
    {
        printf("init failed\n");
        return -1;
    }

    const clock_t start = clock();
    getprime(&primeList);
    int s = 0;
    for (int i = 0; i < primeList.size; i++)
    {
        s += primeList.pdata[i];
        //s += *(primeList.pdata + i);
    }
    printf("%d\n", s);
    const clock_t end = clock();
    printf("%.3f seconds", (end - start) / (double)CLOCKS_PER_SEC);

    list_destroy(&primeList);

    return 0;
}
