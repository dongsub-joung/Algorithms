#include<stdio.h>

int main(void)
{
	int a[][3] = { {12,32,45},
	{45,34,22},
	{61,78,15},
	{52,28,19} };
	int i, j;

	for (i = 0; i < 4; i++) {
		int sum = 0;
		for (j = 0; j < 3; j++) {
			sum += a[i][j];
		}
		printf("%d행의 합:%d\n", i + 1, sum);
	}

	printf("\n\n");

	for (j = 0; j < 3; j++) {
		int sum = 0;
		for (i = 0; i < 4; i++) {
			sum += a[i][j];
		}
		printf("%d열의 합:%d\n", j + 1, sum);
	}

	return 0;
}