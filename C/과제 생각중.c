#include<stdio.h>
#define SIZE=3

int sumup(int sum[][], int size);

int main(void)
{
	int i, j;
	int sum = 0;
	int a[][3] = { {12,35,45},
			{45,34,22},
			{61,78,15},
			{52,28,19} };

	sum = sumup(a, 12);

	printf("%d행의 %d열의 합%d \n", i, j, sum);

	return 0;
}

int sumup(int sum[][SIZE], int size)
{
	int i, j;
	int result = 0;

	for (i = 0; i < 1; i++)
	{
		for (j = 0; j < 3; j++)
		{
			result += a[i][j];
		}
	}
	return result;
}