#include<stdio.h>
int addition(int n);

int main()
{
	int n;
	printf("1���� n������ ���� ���ϴ� ���α׷��Դϴ�. n��?");
	scanf_s("%d", &n);
	printf("1���� %d������ ���� %d�Դϴ�.\n", n, addition(n));
	
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