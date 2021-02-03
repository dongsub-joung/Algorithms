#include "Sub.h"

Subing::Subing()
	:x(),
	y(),
	sum()
{
	0, 0, 0;
}

void Subing::subX_Y(int x, int y)
{
	this->sum = x - y;
}

void Subing::printSum()
{
	std::cout << "subing result" << Subing::sum << std::endl;
}