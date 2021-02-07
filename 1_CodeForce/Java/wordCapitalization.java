package code;
// https://www.techrcoding.com/2020/07/codeforces-281a.html

import java.util.Scanner;

public class wordCapitalization {
    public static void main(String[] args) {
        int i= 0;
        int MAX_LENGTH= 1000;

        Scanner sc= new Scanner(System.in);
        String str= sc.next();
        char[] chr= str.toCharArray();

        int str_len= str.length();
//      The length of the word will not exceed 10^3.
        if (str_len<MAX_LENGTH)
        {
//          처음 대문자 + [1]부터 끝까지 출력
            char first= Character.toUpperCase(chr[0]);
            String result= str.substring(1);
            System.out.println(first+result);
        }
    }
}