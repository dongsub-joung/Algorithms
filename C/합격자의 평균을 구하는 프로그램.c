#include<stdio.h>
#define N 5
double compute_ave(int ary[N]);

int main()
{
	int i;
	int pass = 0, sum = 0; //합격자 수, 합격자 점수의 합
	int score[N] = { 93,82,49,55,75 }; //N명의 점수
	printf("전체 평균: %.1lf\n", compute_ave(score));

	for (i = 0; i < N; i++) {
		if (score[i] >= 60) {
			sum += score[i];
			pass++;
		}
	}
	printf("합격자의 평균:%.1lf\n", (double)sum / pass);
	return 0;
}
double compute_ave(int ary[N])
{
	int i, sum = 0;
	
	for (i = 0; i < N; i++)
		sum += ary[i];

	return (double)sum / N;
}