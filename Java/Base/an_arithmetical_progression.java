package ex1;

import java.util.Scanner;

public class an_arithmetical_progression {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		// ���� �ٸ� �ڿ��� 2���� �޾Ƶ鿩 �� ���̿� �����ϴ� �ڿ����� �հ� 3�� ����� ������ ���� ���Ͽ� ���
		
		int A,B; //���� �ٸ� �ڿ��� 2��
		int N;	//�ݺ� ����
		int MOD;	//3�� ��� �Ǻ� ����
		int CNT=0; //3�� ��� ī��Ʈ
		
		int SUM=0;	//�� ���� ��
		int DOUBLE_SUM=0;	//3�� ����� ������ ��
		
		Scanner stdInput=new Scanner(System.in); //=scanf
		A=stdInput.nextInt();
		B=stdInput.nextInt();
		
		int TEMP;
		if(A>B) {
			TEMP=A;
			A=B;
			B=TEMP;
		}
		
		for(N=A; N<=B; N++) {
			SUM+=N;

		MOD=N%3;
		if(MOD==0) {
			DOUBLE_SUM=DOUBLE_SUM+N*N;
			CNT+=1;
			}
		}
		
		System.out.println("�� �� ������ �ڿ������� ��"+SUM);
		System.out.println("3�� ����� ������ ��"+DOUBLE_SUM);
	}

}
