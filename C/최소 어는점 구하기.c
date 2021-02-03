#include <stdio.h>
#define SIZE 5

int find_min(int arr[]);
void print_arr(int arr[]);

int main()
{
	int f[SIZE] = { 3,0,30,-20,-1 };
	int min;

	min = find_min(f); //최솟값 구하기
	
	printf("어는 점 목록:");
	print_arr(f); //배열 내용 출력하기

	//최솟값 출력하기	
	printf("\n가장 낮은 어는 점:%d\n", min);

	return 0;
}
int find_min(int arr[])//배열의 최솟값을 구하는 함수
{
	int i, min;

	min = arr[0];
	for (i = 1; i < SIZE; i++) {
		if ((arr[i]) < min)
			min = arr[i];
	}
	return min;
}

void print_arr(int arr[]) //배열 원소 출력 함수
{
	int i;
	for (i = 0; i < SIZE; i++) {
		printf("%4d", arr[i]);
	}
}