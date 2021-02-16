import java.util.Scanner;

public class Soldier_and_Bananas {
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        int[] k= new int[1000+1];

        k[0]= sc.nextInt();
        long n= sc.nextLong();
        int w= sc.nextInt();

        int sum= 0;
        long result= 0;
//      Calculating banana price && Adding each price
        for (int i= 1; i<=w; i++) k[i]= k[0]*i;
//      Sum up price
        for (int i= 1; i<=w; i++) sum+= k[i];
        result= sum-n;

        if (n>sum) System.out.println(0);
        else System.out.println(result);
    }
}
