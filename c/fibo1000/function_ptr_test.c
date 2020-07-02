#include <stdio.h>
#include <math.h>
#define PI 3.141592

typedef struct
{
	void* vptr;
	double x;
	double y;
} Shape;

typedef struct
{
	double (*area)(Shape const* const me);
}ShapeVtbl;

double Shape_area(Shape const* const me) {
	//assert(0);
	return 0;
}

ShapeVtbl const Shape_vtbl =
{
	&Shape_area
};

void Shape_init(Shape* const me, double x, double y)
{
	me->vptr = (void*)&Shape_vtbl;
	me->x = x;
	me->y = y;
}

typedef struct
{
	Shape super;
	double r;
} Circle;

double cir_area(Circle const* const me) {
	//Circle const* const me_ = (Circle const*)me;
	double a = PI * pow(me->r, 2);
	return a;
}

ShapeVtbl const Circle_vtbl = {
   &cir_area
};

void Circle_init(Circle* const me, double x, double y, double r) {
	Shape_init(&me->super, x, y);
	me->super.vptr = (void*)&Circle_vtbl;
	me->r = r;
}

typedef struct
{
	Shape super;
	double w;
	double h;
} Rectangle;

double rect_area(Rectangle const* const me)
{
	//Rectangle const* const me_ = (Rectangle const*)me;
	double a = (me->w) * (me->h);
	return a;
}

ShapeVtbl const Rect_vtbl = {
   &rect_area
};

void Rectangle_init(Rectangle* const me, double x, double y, double w, double h)
{
	Shape_init(&me->super, x, y);
	me->super.vptr = (void*)&Rect_vtbl;
	me->w = w;
	me->h = h;
}

double calc_area(Shape const* const me)
{
	ShapeVtbl* pvtable = (ShapeVtbl*)me->vptr;
	return (*pvtable->area)(me);
}

int main(void)
{
	printf("function pointer test\n");

	Circle circle;
	Circle_init(&circle, 0.0, 0.0, 1.0);
	Rectangle rect;
	Rectangle_init(&rect, 10.0, 10.0, 20.0, 3.0);

	Shape* pshape = (Shape*)&circle;
	printf("%lf\n", calc_area(pshape));

	pshape = (Shape*)&rect;
	printf("%lf\n", calc_area(pshape));

	return 0;
}
