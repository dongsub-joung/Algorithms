package code;
// https://itisadumbblog.blogspot.com/2015/07/codeforces-112a-petya-and-strings_1.html
import java.util.Scanner;

public class petyaAndStrings {
    public static void main(String[] args) {
        String first, second, upper_first, upper_second;
        Scanner sc= new Scanner(System.in);

        while (sc.hasNext())
        {
            first= sc.next();
            second= sc.next();

            if (first.compareToIgnoreCase(second)>0) System.out.println(1);
            else if (first.compareToIgnoreCase(second)<0) System.out.println(-1);
            else System.out.println(0);
        }
    }
}

// 1.
//    Scanner sc= new Scanner(System.in);
//    String first_str= sc.nextLine().toLowerCase();
//    String second_str= sc.nextLine().toLowerCase();
//
//    char[] first_arr= first_str.toCharArray();
//    char[] second_arr= second_str.toCharArray();
//
//    int[] sum= new int[2];
//
//    for (char value: first_arr) sum[0] += value;
//    for (char value: second_arr) sum[1] += value;
//
//    if(sum[0]<sum[1]) System.out.println(-1);
//    else if(sum[0] == sum[1]) System.out.println(0);
//    else System.out.println(1);


//  pseudo code
//   String -> uppercase
//      if (char > 58) char - 32
//      sum char[]
//      compare strings