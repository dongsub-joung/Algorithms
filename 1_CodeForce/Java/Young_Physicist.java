//  https://www.techrcoding.com/2020/07/codeforces-69a.html

import java.util.Scanner;

public class Young_Physicist {
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        int n= sc.nextInt();

        int index=0;
        int x=0, y=0, z=0;
        while(index<n)
        {
            int a= sc.nextInt();
            int b= sc.nextInt();
            int c= sc.nextInt();

            x+= a;
            y+= b;
            z+= c;
            index++;
        }

        if (x==0 && y==0 && z==0) System.out.println("YES");
        else System.out.println("NO");
    }
}