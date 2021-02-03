#pragma once
#include <string>
#include <iostream>

class Subing
{
public:
	Subing();

	void subX_Y(int x, int y);
	void printSum();

private:
	int x;
	int y;
	int sum;
};