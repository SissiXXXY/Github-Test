#include <stdio.h>

typedef struct
{
    double x;
    double y;
} Shape;

typedef struct
{
    double x;
    double y;
    double r;
} Circle;

typedef struct
{
    double x;
    double y;
    double w;
    double h;
} Rectangle;

double calc_area(Shape* pshape)
{
    // TODO
    return 0;
}

int main(void)
{
    printf("function pointer test\n");

    Circle circle = { 0,0,1 };
    Rectangle rect = { 10,10,20,3 };

    Shape* pshape = (Shape*)&circle;
    printf("%lf\n", calc_area(pshape));

    pshape = (Shape*)&rect;
    printf("%lf\n", calc_area(pshape));

    return 0;
}
