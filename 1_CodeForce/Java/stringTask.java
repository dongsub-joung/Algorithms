package code;
// https://dorhubs.blogspot.com/2019/07/codeforces-118-problem-solution.html

import java.util.Scanner;

public class stringTask {
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        String str= sc.nextLine();
        char[] arr= str.toCharArray();
        String p= "";

        int len= arr.length;
        for (int i=0; i<len; i++)
        {
            // A(65)~Z(90)
            if(arr[i]<97)  arr[i]= (char) (arr[i]+'a'-'A');  // 97(a), char+97-65,
            if(arr[i]=='a' || arr[i]=='e' || arr[i]=='i' || arr[i]=='o' || arr[i]=='u' || arr[i]=='y') continue;
            else p= p + "." + arr[i];
        }

        System.out.println(p);
    }
}

