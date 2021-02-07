package code;
// https://www.techrcoding.com/2020/07/codeforces-339a.html

import java.util.Scanner;

public class helpfulMaths {
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        String str= sc.nextLine();
        char[] chrs= str.toCharArray();
        char temp= '\0';

        int str_len= str.length();
        for (int i=0; i<str_len-2; i++)
        {
//            System.out.println("i: "+i);
            for (int j= i+2; j<str_len; j++)
            {
//                System.out.println("j: "+j);
//              0,1,2 ... 정수 비교
                if (j%2 == 0)
                {
//                  아스키코드 비교 후, Swap
                    if ( (int) chrs[i]> (int) chrs[j] )
                    {
                        temp= chrs[i];
                        chrs[i]= chrs[j];
                        chrs[j]= temp;
                    }
                }
            }
        }

        String str_2= new String(chrs);
        System.out.println(str_2);
    }
}

// pseudo code
//  extract: interval 2 char arr
//  convert int arr
//  정렬 후 삽입, 출력