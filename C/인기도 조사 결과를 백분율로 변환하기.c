#include<stdio.h>
#define N 4

void print_arr(int arr[N]);
void percentage(int arr[N]);

int main()
{
	int count[N] = { 42,37,83,33 };
	
	printf("�ο���:");
	print_arr(count); //�迭 ���� ���� ���

	percentage(count); //�ο����� ������� ����

	printf("\n �����:");
	print_arr(count); //������� ����� �迭 ���� ���
	return 0;
}

void print_arr(int arr[N]) //int arr[]�� ����
{
	int i;

	for (i = 0; i < N; i++) {
		printf("%3d", arr[i]);
	}
}

void percentage(int arr[N])
{
	int i, total = 0;
	//���� ���� ��ü �ο� total ���ϱ�
	for (i = 0; i < N; i++) {
		total += arr[i];
	}
		//����� ���ϱ�
		for (i = 0; i < N; i++) {
			arr[i] = (int)((double)arr[i] / total * 100);
		}
	
}