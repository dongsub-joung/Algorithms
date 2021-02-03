#include<stdio.h>
#define N 5

void exchange(int* arr, int size);
void prt_array(int* arr, int size);

int main(void)
{
	int array[N] = { 5,7,1,3,9 };
	printf("정렬 전\n");
	prt_array(array, N);
	exchange(array, N);
	printf("정렬 후\n");
	prt_array(array, N);

	return 0;
}

void exchange(int* arr, int size)
{
	int i, j;
	int temp = 0;

	for(i=0;i<N-1;i++)
		for(j=i+1;j<N;j++)
			if (arr[i] > arr[j]) {
				temp = arr[i];
				arr[i] = arr[j];
				arr[j] = temp;
			}
	return 0;
}

void prt_array(int* arr, int size)
{
	int i;
	for (i = 0; i < N; i++)
		printf("array[]=%d\n", arr[i]);

	return 0;
}