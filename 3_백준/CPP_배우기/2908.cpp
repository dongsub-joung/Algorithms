#include <iostream>
#include <string>

using namespace std;

// https://seoftware.tistory.com/8
int main(void)
{
	string x, y;
	cin >> x >> y;

	string bigger;

	for (int i = 2; i >= 0; i--)
	{
		if (x[i] > y[i])
		{
			bigger = x; break;
		}
		else if (x[i] < y[i])
		{
			bigger = y; break;
		}
	}

	cout << bigger[2] << bigger[1] << bigger[0];
	return 0;
}

	// https://www.javatpoint.com/cpp-program-to-reverse-number
	// int n, rem;
	// int reverse = 0;
	// cout << "Enter a number: ";
	// cin >> n;

	// while (n!=0)
	// {
	// 	rem = n % 10;	// 10으로 나눈 나머지
	// 	reverse = reverse * 10 + rem;
	// 	n /= 10;
	// }
	// cout << "Reversed Number: " << reverse << endl;
	// return 0;


	// 				1차
	// int a = 0;
	// int b = 0;
	// cin >> a, b;

	// string string_a= to_string(a);
	// string string_b= to_string(b);

	// reverse(string_a.begin(), string_a.begin());
	// reverse(string_b.begin(), string_b.begin());
	
	// int x = stoi(string_a);
	// int y = stoi(string_b);

	// if (x > y)
	// {
	// 	printf("%d", x);
	// }
	// else
	// {
	// 	printf("%d", y);
	// }