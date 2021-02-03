#include<stdio.h>
#define N 5

void selection(int* arr, int size);
void prt_array(int* arr, int size);

int main(void)
{
	int array[N] = { 5,7,1,3,9 };
	printf("정렬 전\n");
	prt_array(array, N);

	selection(array, N);
	printf("정렬 후\n");

	prt_array(array, N);

	return 0;
}

void selection(int* arr, int size)
{
	int i, j;
	int index = 0;

	for (i = 0; i < N - 1; i++) {
		index = i;
		for (j = i + 1; j < N; j++) {
			if (arr[index] > arr[j])
				index = j;
		}
	int temp;
	temp = arr[i];
	arr[i] = arr[index];
	arr[index] = temp;

	}
	return 0;
}

void prt_array(int* arr, int size)
{
	int i;
	for (i = 0; i < N; i++)
		printf("arr[]=%d\n", arr[i]);

	return 0;
}