import java.util.Scanner;

public class WrongSubtraction {

    public static void main(String[] args) {

        Scanner sc= new Scanner(System.in);
        long n= sc.nextInt();
        int k= sc.nextInt();
        long calculated= 0;

        for (int i=0; i<k; i++)
        {
            calculated= n%10;

            if (calculated != 0)
            {
                n-= 1;
            }
            else if (calculated == 0)
            {
                n/= 10;
            }
        }

        System.out.println(n);
    }
}