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

	printf("��ǻ�Ͱ� ���� ���� ã�� ����\n");
	printf("========================================================");
	
	do
	{
		printf("%3d~%3d ���� ���Դϴ�. ����?",  begin,end);
		scanf_s("%d", &user);

		count++;

		if(user>com)
			end=user-1;
		else if(user<com)
			begin=user+1;

	}while (user !=com);

	printf("======================");
	printf("��ǻ�Ͱ� ���� %d�� %d���� �­����ϴ�.\n", com, count);

	return 0;
}