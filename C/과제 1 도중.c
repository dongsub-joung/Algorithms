#include<stdio.h>

int main(void)
{
	int i, j;
	int sum = 0;
	int a [][3] = { {12,35,45},
			{45,34,22},
			{61,78,15},
			{52,28,19} };

	int sum_up[2];

	for (i = 0; i < 4; i++)
	{
		for (j = 0; j < 3; j++)
		{
			sum += a[i][j];
			
			if (i == 0 && j == 2)
				printf("0���� �հ�%d", sum);
			else if (i == 1 && j == 2)
				printf("1���� �հ�%d", sum);
			else if (i == 2 && j == 2)
				printf("2���� �հ�%d", sum);
			else if (i == 3 && j == 2)
				printf("3���� �հ�%d", sum);
			else if (i == 4 && j == 2)
				printf("4���� �հ�%d", sum);
		}
	}
}
