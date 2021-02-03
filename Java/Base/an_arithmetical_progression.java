package ex1;

import java.util.Scanner;

public class an_arithmetical_progression {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		// 서로 다른 자연수 2개를 받아들여 그 사이에 존재하는 자연수의 합과 3의 배수의 제곱의 합을 구하여 출력
		
		int A,B; //서로 다른 자연수 2개
		int N;	//반복 변수
		int MOD;	//3의 배수 판별 변수
		int CNT=0; //3의 배수 카운트
		
		int SUM=0;	//두 수의 합
		int DOUBLE_SUM=0;	//3의 배수의 제곱의 합
		
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
		
		System.out.println("두 수 사이의 자연수들의 합"+SUM);
		System.out.println("3의 배수의 제곱의 합"+DOUBLE_SUM);
	}

}
