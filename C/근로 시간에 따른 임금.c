#include<stdio.h>

int get_pay(int hours, int day_rate, int hour_rate);

int main()
{
	int total_hours;
	int daily_rate = 100000, hourly_rate = 10000;
	int pay;

	printf("�ٷ� �ð���?");
	scanf_s("%d\n", &total_hours);
	pay = get_pay(total_hours, daily_rate, hourly_rate);
	printf("�� �Ϸ� �ӱ��� %d��\n", pay);

	return	0;
}

int get_pay(int hours, int day_rate, int hour_rate)
{
	int day = hours / 8;
	hours = hours % 8;

	return (day * day_rate + hours * hour_rate);
}