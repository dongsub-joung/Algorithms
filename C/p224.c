#include<stdint.h>

int main(void)
{
	int	i, j, sum = 0;
	int a[][3] = { {90,80,90},	//영희의 국어,영어,수학 점수
				{70,100,100},//철수의 국어,영어,수학점수
				{80,90,90} }; //미나의 국어,영어, 수학점수

	double average[3];

	for (i = 0; i < 3; i++)
	{
		for (j = 0; j < 3; j++)
		{
			sum += a[i][j];
		}

		average[i] = (double)sum / j;
		printf("%d번 학생의 평균은 %.2lf\n", i + 1, average[i]);

		//다음 학생의 평균을 구하기 위해 sum을 초기화한다.
		sum = 0;
	}

	return	0;
}