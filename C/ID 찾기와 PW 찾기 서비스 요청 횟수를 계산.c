#include<stdio.h>

void find_PW();
void find_ID();

char title[10] = "Quize"; //���Ӹ� ���� ����

static int count_service; //�� ���� ��û Ƚ��, ���� ���� ����

int main()
{
	int service; //����ڰ� ��û�� ���� ��ȣ, main�� ���� ����
	do
	{
		printf("\n<<<1. IDã�� 2.PWã�� 3.�����ϱ� >>>\n");
		printf("���ϴ� ���� ��ȣ�� �Է��ϼ���(1~3)");
		scanf_s("%d", &service);
		switch (service)
		{
		case 1:find_ID(); break;
		case 2:find_PW();
		}
	} while (service != 3); //3�����ϱ⸦ �������� �ʴ� �� ��� �ݺ��ϱ�
	return 0;
}

void find_ID()
{
	static int count_ID; //�Լ��� ȣ�� Ƚ���� ����, ���� ���� ����

	count_ID++; //�Լ��� ȣ��ɶ����� 1�� ����
	count_service++; //��ü ���� ��û ȸ���� 1����

	printf("\n %s ���� �湮 ��", title);
	printf("�� ��ü ���� ��û %d�� �� %dȸ° IDã�� ��û�Դϴ�.\n",
		count_service, count_ID);
}

void find_PW()
{
	static int count_PW; //�� �Լ��� ȣ�� Ƚ���� �����ϴ� ���� ���� ���� ����
	
	count_PW++;
	count_service++;

	printf("\n %s ���� �湮 ��", title);
	printf("�� ��ü ���� ��û%d�� �� %dȸ° PWã�� ��û�Դϴ�.\n",
		count_service, count_PW);
}