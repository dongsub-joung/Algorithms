package code;
// https://www.techrcoding.com/2020/07/codeforces-266a.html

import java.util.Scanner;

public class StonesOnTheTable {
    public static void main(String[] args) {
        int cnt= 0;
        Scanner sc= new Scanner(System.in);

        int MAX_SIZE= sc.nextInt();
        String stones= sc.next();
        char[] colors= stones.toCharArray();
        int len_stones= stones.length();

        if (MAX_SIZE == stones.length())
        {
            for (int i=0; i< len_stones-1; i++)
            {
                if (colors[i] == colors[i+1]) cnt++;
            }
        }
        System.out.println(cnt);
    }
}

// pseudo code
//  String -> charArray
//  for(value:charArray)
//      if value == char[i-1] cnt++
//      else if value == char[i+1] cnt++

// 1~3 pivot 양쪽을 비교함..
//  1.
//        for (char value:colors)
//        {
//            if (i!=0)
//            {
//                if (value == colors[i-1]) cnt++;
//            }
//            if (value == colors[i+1]) cnt++;
//            else continue;
//            i++;
//        }


//  2.
//        do
//        {
//            char value= colors[i];
//            if (i!=0)
//            {
//                if (value == colors[i-1]) cnt++;
//            }
//
//            if (value == colors[i+1]) cnt++;
//            else continue;
//            i++;
//        }while (i>=MAX_SIZE);


//  3.
//        for (int i= 0; i<MAX_SIZE; i++)
//        {
//        char value= colors[i];
//        if(i == 0 || i == MAX_SIZE-1) continue;
//
//        else if (value == colors[i-1]) cnt++;
//        else if (value == colors[i+1]) cnt++;
//        else continue;
//        }