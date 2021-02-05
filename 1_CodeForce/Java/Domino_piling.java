package project1;

import java.util.Scanner;

public class Domino_Piling 
{
	public static void main(String[] args)
	{
		Scanner scanner= new Scanner(System.in);
		double M= scanner.nextInt();
		double N= scanner.nextInt();
		double innerSize= M*N;
		int result= (int)Math.floor(innerSize/2);
		System.out.println(result);
	}
}
