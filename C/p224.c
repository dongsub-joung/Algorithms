#include<stdint.h>

int main(void)
{
	int	i, j, sum = 0;
	int a[][3] = { {90,80,90},	//������ ����,����,���� ����
				{70,100,100},//ö���� ����,����,��������
				{80,90,90} }; //�̳��� ����,����, ��������

	double average[3];

	for (i = 0; i < 3; i++)
	{
		for (j = 0; j < 3; j++)
		{
			sum += a[i][j];
		}

		average[i] = (double)sum / j;
		printf("%d�� �л��� ����� %.2lf\n", i + 1, average[i]);

		//���� �л��� ����� ���ϱ� ���� sum�� �ʱ�ȭ�Ѵ�.
		sum = 0;
	}

	return	0;
}