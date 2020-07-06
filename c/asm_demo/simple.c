#include <stdio.h>

int f0(int a, int b)
{
    return a + b;
}

int f1(int a, int n)
{
    int f1_x = 1;
    if (a > 0)
        return f1_x + a + n;
    else
        return f1_x - a - n;
}

void f2(int a, int b)
{
    int f2_x = f1(a, 10);
    printf("call f1(a,10) --> %d\n", f2_x);

    int f2_y = f1(b, 1000);
    printf("call f1(b,1000) --> %d\n", f2_y);
}

int main()
{
    int main_v1 = f0(1234, 5678);
    f2(main_v1, 456);
    return 0;
}
