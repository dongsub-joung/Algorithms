#include <stdio.h>
#include <math.h>//sqrt,pow함수를 위한 헤더 파일
#define N 5

double compute_avg(int arr[]);
double compute_s(int arr[]);

int main()
{
	int i, kor[N] = { 90,89,47,78,90 };
	int music[N] = { 99,98,86,75,100 };
	 
	printf("평균: %5.1lf %5.1lf\n",
		compute_avg(kor), compute_avg(music));
	printf("표준편차:%5.1lf %5.1lf\n",
		compute_s(kor), compute_s(music));

	return 0;
}

double compute_s(int arr[])
{
	int i;
	double sum, avg;

	avg = compute_avg(arr);

	sum = 0;
	for (i = 0; i < N; i++)
		sum = sum + pow(arr[i] - avg, 2);
	return sqrt(sum / N);
}

double compute_avg(int arr[])
{
	int i, sum = 0;

	for (i = 0; i < N; i++) {
		sum = sum + arr[i];
	}
		return (double)sum / N;
	
}