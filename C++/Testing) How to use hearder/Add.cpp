#include "Add.h"

Adding::Adding()
	:x(),
	y(),
	m_sum()
{}

void Adding::Add_X_Y(int x, int y)
{
	m_sum = x + y;
}

void Adding::Print()
{
	int* ptr = &m_sum;
	std::cout << *ptr << std::endl;
}