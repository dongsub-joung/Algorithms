#include <stdio.h>
#include <stdlib.h> //rand, srand
#include <time.h>  //time 함수를 위한 헤더 파일

int main()
{
	int begin = 1, end = 100; //컴퓨터가 숨길 값 범위
	int count = 0; //답 맞히기 시도 횟수
	int computer, user; //컴퓨터가 숨긴 값, 사용자 추측 값

	srand(time(NULL)); //현재 시간을 씨드로 설정

	computer = rand() % (end - begin + 1) + 1; //스케일링


	printf("\n>>컴퓨터가 숨긴 수를 맞히는 게임입니다. \n");
	printf("\n===============================================\n");

	do
	{
		printf("%3d~%3d 중의 값입니다. 얼마일까요?", begin, end);
		scanf_s("%d", &user);

		count++; //시도 횟수 1증가

		//숨긴 수의 범위 수정
		if (user > computer)
			end = user - 1;
		else if (user < computer)
			begin = user + 1;
	} while (user != computer); //추측 값이 틀리면 다시 반복

	printf("==============================================\n");
	printf("\n컴퓨터가 숨긴 %d를 %d번 만에 맞혔습니다.", computer, count);

	return 0;
}