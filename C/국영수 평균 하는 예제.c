#include<stdio.h>

int main(void)
{
	int i, j, sum = 0;
	int a[][3] = { {90,80,90}, //������ ����, ���� , ���� ����
	{70,100,100}, //ö���� ����,����, ���� ����
	{80,90,90} }; //�̳��� ����,����, ���� ����

	double aveClass[3];

	for (j = 0; j < 3; j++)
	{
		for (i = 0; i < 3;i++)
		{
			sum += a[i][j];
		}

		aveClass[j] = (double)sum / i;

			if (j == 0)
				printf("���� ����� %.2lf�̴�.\n", aveClass[j]);
			else if (j == 1)
				printf("���� ����� %.2lf�̴�.\n", aveClass[j]);
			else if (j == 2)
				printf("���� ����� %.2lf�̴�.\n", aveClass[j]);

		//���� ������ ����� ���ϱ� ���ؼ� sum�� �ʱ�ȭ�Ѵ�.
		sum = 0;
	}

	return 0;
}