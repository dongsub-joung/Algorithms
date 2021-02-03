#include<stdio.h>

void find_PW();
void find_ID();

char title[10] = "Quize"; //게임명 전역 변수

static int count_service; //총 서비스 요청 횟수, 정적 전역 변수

int main()
{
	int service; //사용자가 요청한 서비스 번호, main의 지역 변수
	do
	{
		printf("\n<<<1. ID찾기 2.PW찾기 3.종료하기 >>>\n");
		printf("원하는 서비스 번호를 입력하세요(1~3)");
		scanf_s("%d", &service);
		switch (service)
		{
		case 1:find_ID(); break;
		case 2:find_PW();
		}
	} while (service != 3); //3종료하기를 선택하지 않는 한 계속 반복하기
	return 0;
}

void find_ID()
{
	static int count_ID; //함수의 호출 횟수를 저장, 정적 지역 변수

	count_ID++; //함수가 호출될때마다 1씩 증가
	count_service++; //전체 서비스 요청 회수를 1증가

	printf("\n %s 게임 방문 중", title);
	printf("총 전체 서비스 요청 %d번 중 %d회째 ID찾기 요청입니다.\n",
		count_service, count_ID);
}

void find_PW()
{
	static int count_PW; //이 함수의 호출 횟수를 저장하는 정적 지역 변수 선언
	
	count_PW++;
	count_service++;

	printf("\n %s 게임 방문 중", title);
	printf("총 전체 서비스 요청%d번 중 %d회째 PW찾기 요청입니다.\n",
		count_service, count_PW);
}