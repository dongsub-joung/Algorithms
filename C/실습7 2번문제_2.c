#include<stdio.h>

float  avg(float  num1, float  num2);

int main(void)
{
	float  x, y;
	float  result_avg = 0;

	printf("�Ǽ� �ΰ��� �Է��Ͻÿ�.\n");
	scanf_s("%f %f", &x, &y);

	result_avg = avg(x, y);

	printf("%.2lf��%.2lf�� �����%.2lf \n", x, y, result_avg);

	return 0;
}

float  avg(float  num1, float  num2)
{
	float  A = 0;

	A = (num1 + num2) / 2;

	return A;
}