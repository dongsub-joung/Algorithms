#include<stdio.h>
#define SIZE 5

int main()
{
	int i, u;
	int kor[SIZE] = { 90, 80, 70, 60, 100 };
	int math[SIZE] = { 81,91,81,81,100 };
	int order[SIZE];
	double avg[SIZE];

	for (i = 0; i < SIZE; i++)
	{
		avg[i] = (double)(kor[i] + math[i] / 2);
	}

	for (i = 0; i < SIZE; i++)
	{
		order[i] = 1;
		for (u = 0; u < SIZE; u++)
		{
			if (avg[i] < avg[u])
				order[i]++;
		}
	}
	printf("========================================\n");
	printf("국어\t 수학 \t 평균\t 석차\t\n");
	printf("========================================\n");
	for (i = 0; i < SIZE; i++)
	{
		printf("%5d %7d\ %8.2lf %5d\n", kor[i], math[i], avg[i], order[i]);
	}
	printf("==========================================\n");

	return	0;
}