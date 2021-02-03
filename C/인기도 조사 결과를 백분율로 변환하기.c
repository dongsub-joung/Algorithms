#include<stdio.h>
#define N 4

void print_arr(int arr[N]);
void percentage(int arr[N]);

int main()
{
	int count[N] = { 42,37,83,33 };
	
	printf("인원수:");
	print_arr(count); //배열 원래 내용 출력

	percentage(count); //인원수를 백분율로 변경

	printf("\n 백분율:");
	print_arr(count); //백분율로 변경된 배열 내용 출력
	return 0;
}

void print_arr(int arr[N]) //int arr[]도 가능
{
	int i;

	for (i = 0; i < N; i++) {
		printf("%3d", arr[i]);
	}
}

void percentage(int arr[N])
{
	int i, total = 0;
	//조사 참여 전체 인원 total 구하기
	for (i = 0; i < N; i++) {
		total += arr[i];
	}
		//백분율 구하기
		for (i = 0; i < N; i++) {
			arr[i] = (int)((double)arr[i] / total * 100);
		}
	
}