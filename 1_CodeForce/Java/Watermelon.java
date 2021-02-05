import java.util.Scanner;
public class Watermelon
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int inputed_num= sc.nextInt();
        int divided= inputed_num%2;
        String result= (divided == 0 && inputed_num != 2) ? "YES" : "NO";
        System.out.println(result);
    }
}