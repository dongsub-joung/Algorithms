#include<stdio.h>
int addition(int n);

int main()
{
	int n;
	printf("1에서 n가지의 합을 구하는 프로그램입니다. n은?");
	scanf_s("%d", &n);
	printf("1에서 %d까지의 합은 %d입니다.\n", n, addition(n));
	
	return 0;
}

int addition(int n)
{
	int result;

	if (n > 1)
		result = addition(n - 1) + n;
	else
		result = 1;

	return result;
}