#include<stdio.h>
int find_larger(); //�Լ� ���� ����
int n1, n2, max; //���� ���� ����

int main()
{
	printf("ù�� ����?"); scanf_s("%d", &n1);
	printf("��° ����?"); scanf_s("%d", &n2);

	max = find_larger();

	printf("n1=%d, n2=%d �� ū ���� %d\n", n1, n2, max);

	return 0;
}
// ���� ���� n1,n2 �� ū ���� ��ȯ�ϴ� find_larger�Լ�
int find_larger()
{
	if (n1 > n2)
		return n1;
	else
		return n2;
}