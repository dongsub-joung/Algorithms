#include<stdio.h>
#define N 5
double compute_ave(int ary[N]);

int main()
{
	int i;
	int pass = 0, sum = 0; //�հ��� ��, �հ��� ������ ��
	int score[N] = { 93,82,49,55,75 }; //N���� ����
	printf("��ü ���: %.1lf\n", compute_ave(score));

	for (i = 0; i < N; i++) {
		if (score[i] >= 60) {
			sum += score[i];
			pass++;
		}
	}
	printf("�հ����� ���:%.1lf\n", (double)sum / pass);
	return 0;
}
double compute_ave(int ary[N])
{
	int i, sum = 0;
	
	for (i = 0; i < N; i++)
		sum += ary[i];

	return (double)sum / N;
}