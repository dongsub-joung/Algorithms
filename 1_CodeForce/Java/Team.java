package test;

import java.util.Scanner;

public class Team
{
    public static void main(String[] args)
    {
        Scanner sc= new Scanner(System.in);
        int count = sc.nextInt();

        int pass= 0;
        for (int i = 0; i < count; i++)
        {
            int Petya;
            int Vasya;
            int Tonya;

            Petya= sc.nextInt();
            Vasya= sc.nextInt();
            Tonya= sc.nextInt();

            int dicisions= Petya+Vasya+Tonya;
            if(dicisions >= 2) pass++;
        }

        System.out.println(pass);
    }
}
//        3
//        1 1 0
//        1 1 1
//        1 0 0
//        > 2
