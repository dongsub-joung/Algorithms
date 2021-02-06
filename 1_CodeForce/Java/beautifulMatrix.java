package code;

import java.util.Scanner;

public class beautifulMatrix{
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        int MAX_SIZE= 6;
        int[][] arr= new int[MAX_SIZE][MAX_SIZE];
        int i=0, j=0;
        int r= 0, c= 0;

        for(i= 1; i<MAX_SIZE; i++)
        {
            for (j= 1; j<MAX_SIZE; j++)
            {
                arr[i][j]= sc.nextInt();
//                System.out.println(arr[i][j]);
            }
        }

        for (i=1; i<MAX_SIZE; i++)
        {
            for (j=1; j<MAX_SIZE; j++)
            {
                 if(arr[i][j] == 1)
                 {
                     r= i;
                     c= j;
                     System.out.println(Math.abs(r-3) + Math.abs(c-3));
                 }
            }
        }
    }
}
