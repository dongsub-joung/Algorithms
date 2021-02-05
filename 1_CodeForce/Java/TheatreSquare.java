import java.util.Scanner;

public class TheatreSquare
{
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        int n= sc.nextInt();
        int m= sc.nextInt();
        int a= sc.nextInt();
        
        // Math.round()로 반올림을 생각했는데 1이상이면 1블록으로 치니까 납득
        long horizontal= (n/a);
        if(n%a != 0) ++horizontal;

        long vertical= (m/a);
        if(m%a != 0) ++vertical;

        long result= horizontal*vertical;
        System.out.println(result);
    }
}