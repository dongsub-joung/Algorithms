package ex1;

import java.util.Scanner;

public class Pluse_Num {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//�� ���� ���� N1�� N2�� �Է� �޾�(�� N1���� N2�� ũ��), �̵�� �̵� ���̿� �ִ� ������ ���� ���Ͽ� ����϶�.
		
				int N1,N2;	//�� ������ ���� ���� ����
				int SUM=0;	// �� ���� ������ ����
				
				int temp=0;	//�� ������ ũ�⸦ ���߱� ���� ����
				
				Scanner stdInput =new Scanner(System.in); //=scanf
				N1=stdInput.nextInt();
				N2=stdInput.nextInt();
				
				System.out.print("�Է� ���� �ΰ��� ����" +N1); 
				System.out.println(","+N2);
				
				if(N1>N2){	//N2�� N1���� Ŀ����(����1) �׷��� ������ ��ȯ
					temp=N1;
					N1=N2;
					N1=temp;
				}
				
				int N;
				for(N=N1; N<=N2; N++) SUM=SUM+N;	//N1���� �����ؼ� N2���� �ݺ�
				
				System.out.println("�� �������� ����" +SUM); 

		}
}