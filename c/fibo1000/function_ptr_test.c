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
	double (*move)(Shape* const me);
	double (*area)(Shape const* const me);
}ShapeVtbl;

double Shape_area(Shape const* const me) {
	//assert(0);
	return 0;
}

void Shape_move(Shape* const me, double deltax, double deltay) {
	//assert(0);
}


ShapeVtbl const Shape_vtbl =
{
	&Shape_move,
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

void cir_move(Circle* const me, double deltax, double deltay) {
	me->super.x += deltax;
	me->super.y += deltay;

	printf("circle current position: x: %f, y: %f, radius: %f", me->super.x, me->super.y, me->r);
}

ShapeVtbl const Circle_vtbl = {
	&cir_move, 
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

void rect_move(Rectangle* const me,double deltax,double deltay)
{
	me->super.x += deltax;
	me->super.y += deltay;
	printf("circle current position: x: %f, y: %f, width: %f, height: %f", me->super.x, me->super.y, me->w, me->h);
}

ShapeVtbl const Rect_vtbl = {
	&rect_move, 
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

double after_move(Shape *const me, double deltax, double deltay)
{
	ShapeVtbl* pvtable = (ShapeVtbl*)me->vptr;
	return (*pvtable->move)(me);
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
	after_move(pshape, 3.5, 3.5);

	pshape = (Shape*)&rect;
	printf("%lf\n", calc_area(pshape));
	after_move(pshape, 5.0, 5.0);
	
	return 0;
}
