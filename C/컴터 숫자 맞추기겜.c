#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
	int begin=1, end=100;
	int count=0;
	int com, user;
	
	srand (time(NULL));

	com= rand()%(end-begin+1)+1;

	printf("컴퓨터가 숨긴 수를 찾는 게임\n");
	printf("========================================================");
	
	do
	{
		printf("%3d~%3d 중의 값입니다. 얼마임?",  begin,end);
		scanf_s("%d", &user);

		count++;

		if(user>com)
			end=user-1;
		else if(user<com)
			begin=user+1;

	}while (user !=com);

	printf("======================");
	printf("컴퓨터가 숨긴 %d를 %d만에 맞췃습니다.\n", com, count);

	return 0;
}