#include <iostream>
#include <string>
#define MAX 10
using namespace std;

//https://blockdmask.tistory.com/82
int main()
{
	int A, B, C;
	int arr[MAX] = { 0 };
	cin >> A >> B >> C;

	int calculated = A * B * C;
	while (calculated != 0)
	{
		arr[calculated % 10] += 1;
		calculated /= 10;
	}

	for (int i = 0; i < MAX; i++)
	{
		cout << arr[i] << endl;
	}
}