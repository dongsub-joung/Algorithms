#include <stdio.h>
#define SIZE 5

int find_min(int arr[]);
void print_arr(int arr[]);

int main()
{
	int f[SIZE] = { 3,0,30,-20,-1 };
	int min;

	min = find_min(f); //�ּڰ� ���ϱ�
	
	printf("��� �� ���:");
	print_arr(f); //�迭 ���� ����ϱ�

	//�ּڰ� ����ϱ�	
	printf("\n���� ���� ��� ��:%d\n", min);

	return 0;
}
int find_min(int arr[])//�迭�� �ּڰ��� ���ϴ� �Լ�
{
	int i, min;

	min = arr[0];
	for (i = 1; i < SIZE; i++) {
		if ((arr[i]) < min)
			min = arr[i];
	}
	return min;
}

void print_arr(int arr[]) //�迭 ���� ��� �Լ�
{
	int i;
	for (i = 0; i < SIZE; i++) {
		printf("%4d", arr[i]);
	}
}