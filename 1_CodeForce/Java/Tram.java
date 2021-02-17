import java.util.Scanner;

public class Tram {

    public static void main(String[] args) {

        Scanner sc= new Scanner(System.in);
        int n= sc.nextInt();
        int MAX_SIZE= 1000;
        int[] a= new int[MAX_SIZE];
        int[] b= new int[MAX_SIZE];
        int i, max= 0;

        for (i=0; i<n; i++)
        {
            if (i == 0)
            {
                a[i]= sc.nextInt();
                b[i]= sc.nextInt();
            }
            else
            {
                a[i]= sc.nextInt();
                b[i]= sc.nextInt();
                // 탑승객 - 내린 손님
                b[i]+= b[i-1]-a[i];
            }
        }

        for (i=0; i<n-1; i++)
        {
            if (b[i]>max) max= b[i];
        }
        System.out.println(max);
    }
}