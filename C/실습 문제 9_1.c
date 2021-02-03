#include<stdio.h>

int is_prime(int x);

int main(void)
{
	int i;
	for (i = 2; i < 100; i++) {
		if (is_prime(i) == 1)
			printf("%d\n", i);
	}
	return 0;
}

int is_prime(int x)
{
	int i;
	for (i = 2; i < x; i++) {
		if (x % i == 0) return 0;
	}
	return 1;
}