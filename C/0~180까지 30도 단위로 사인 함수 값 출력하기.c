#include<stdio.h>
#include<math.h>
#define PI 3.141592

int main()
{
	int degree; //각도 저장
	double radian; //degree의 라디안 값 저장 변수

	for (degree = 0; degree <= 180; degree += 30) {
		radian = (PI * degree) / 180; //각도 > 라디안
		printf("sin(%d)=%.5lf\n", degree, sin(radian));
	}
	return 0;
}