#include "Add.h"
#include "Sub.h"
#include <string>
#include <iostream>

int main()
{
	Adding a;

	a.Add_X_Y(4, 3);
	a.Print();

	Subing b;

	b.subX_Y(10, 4);
	b.printSum();

	return 0;
}