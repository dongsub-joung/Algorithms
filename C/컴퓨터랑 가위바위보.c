#include <stdio.h>
#include <stdlib.h> //rand, srand
#include <time.h>  //time �Լ��� ���� ��� ����

int main()
{
	int begin = 1, end = 100; //��ǻ�Ͱ� ���� �� ����
	int count = 0; //�� ������ �õ� Ƚ��
	int computer, user; //��ǻ�Ͱ� ���� ��, ����� ���� ��

	srand(time(NULL)); //���� �ð��� ����� ����

	computer = rand() % (end - begin + 1) + 1; //�����ϸ�


	printf("\n>>��ǻ�Ͱ� ���� ���� ������ �����Դϴ�. \n");
	printf("\n===============================================\n");

	do
	{
		printf("%3d~%3d ���� ���Դϴ�. ���ϱ��?", begin, end);
		scanf_s("%d", &user);

		count++; //�õ� Ƚ�� 1����

		//���� ���� ���� ����
		if (user > computer)
			end = user - 1;
		else if (user < computer)
			begin = user + 1;
	} while (user != computer); //���� ���� Ʋ���� �ٽ� �ݺ�

	printf("==============================================\n");
	printf("\n��ǻ�Ͱ� ���� %d�� %d�� ���� �������ϴ�.", computer, count);

	return 0;
}