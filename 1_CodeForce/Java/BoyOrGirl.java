import java.util.Arrays;
import java.util.HashSet;
import java.util.Scanner;

//https://codeforces.com/problemset/problem/236/A

public class BoyOrGirl
{
    public static void main(String[] args)
      {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        countChar(s);
      }

    public static void countChar(String str)
    {
        // int len = str.length();
        // int count= 0;
        // for(int i=0; i<len; i++)
        // {
        //   if(Character.isLetter(str[i]) == true)  string을 배열로 인식하지 않음.
        //   {
        //     count++;
        //   }
        // }
        int len = str.length();
        HashSet<Character> set = new HashSet<>() ;
        for(int i=0 ; i<len; i++)
        {
            char c =  str.charAt(i);
            set.add(c);
        }
        int size = set.size();
        String result =  (size % 2 == 1) ? "IGNORE HIM!" : "CHAT WITH HER!" ;
        System.out.println(result);
    }
}
