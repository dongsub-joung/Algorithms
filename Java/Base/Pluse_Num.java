package ex1;

import java.util.Scanner;

public class Pluse_Num {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//두 개의 정수 N1과 N2를 입력 받아(단 N1보다 N2가 크다), 이들과 이들 사이에 있는 정수의 합을 구하여 출력하라.
		
				int N1,N2;	//두 정수를 받을 변수 선언
				int SUM=0;	// 두 변수 사이의 총합
				
				int temp=0;	//두 정수의 크기를 맞추기 위한 변수
				
				Scanner stdInput =new Scanner(System.in); //=scanf
				N1=stdInput.nextInt();
				N2=stdInput.nextInt();
				
				System.out.print("입력 받은 두개의 정수" +N1); 
				System.out.println(","+N2);
				
				if(N1>N2){	//N2가 N1보다 커야함(조건1) 그렇지 않으면 교환
					temp=N1;
					N1=N2;
					N1=temp;
				}
				
				int N;
				for(N=N1; N<=N2; N++) SUM=SUM+N;	//N1부터 시작해서 N2까지 반복
				
				System.out.println("두 정수간의 합은" +SUM); 

		}
}