import java.util.Scanner;

public class Football {
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        String inputed= sc.next();

        if (inputed.contains("1111111") || inputed.contains("0000000"))
        {
            System.out.println("YES");
        }
        else System.out.println("NO");
    }
}
