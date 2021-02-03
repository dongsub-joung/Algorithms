#include<stdio.h>

int main(void)
{
	int i, j, sum = 0;
	int a[][3] = { {90,80,90}, //영희의 국어, 영어 , 수학 점수
	{70,100,100}, //철수의 국어,영어, 수학 점수
	{80,90,90} }; //미나의 국어,영어, 수학 점수

	double aveClass[3];

	for (j = 0; j < 3; j++)
	{
		for (i = 0; i < 3;i++)
		{
			sum += a[i][j];
		}

		aveClass[j] = (double)sum / i;

			if (j == 0)
				printf("국어 평균은 %.2lf이다.\n", aveClass[j]);
			else if (j == 1)
				printf("영어 편균은 %.2lf이다.\n", aveClass[j]);
			else if (j == 2)
				printf("수학 평균은 %.2lf이다.\n", aveClass[j]);

		//다음 과목의 평균을 구하기 위해서 sum을 초기화한다.
		sum = 0;
	}

	return 0;
}