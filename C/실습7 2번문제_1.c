#include<stdio.h>

int factorial(int x);

int main(void)
{
	int num;
	int num_fac = 0;

	printf("정수 n을 입력\n");
	scanf_s("%d", &num);

	num_fac = factorial(num);

	printf("%d!:%d", num, num_fac);

	return 0;
}

int factorial(int x)
{
	int i;
	int result = 1;

	for (i = 1; i <= x - 1; i++) result *= i;

	return (result * x);
}