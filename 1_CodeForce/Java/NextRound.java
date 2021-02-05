package code;

import java.util.Scanner;

public class NextRound {
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        int n= sc.nextInt();
        int k= sc.nextInt();

        int[] a= new int[n];
        int sum= 0;

        for(int i=0; i<n; i++) a[i]= sc.nextInt();

        int key= a[k-1];
        for(int i=0; i<n; i++)
        {
            if(a[i]>=key && a[i]>0) sum++;
        }
        System.out.println(sum);
    }
}

//  2.
//        Scanner sc= new Scanner(System.in);
//        int n= sc.nextInt();
//        int k= sc.nextInt();
//        int min_score= 0;
//
//        int[] arr= new int[n+1];
//
//        for (int i=0; i<n; i++)
//        {
//            arr[i]= sc.nextInt();
//            if(i == k) min_score= arr[i];
//        }
//
//        int cnt= 0;
//        for(int i=0; i<=n; i++)
//        {
//            if (arr[i]>=min_score && arr[i]>0) cnt++;
//        }
//
//        System.out.println(cnt);

//        1.
//        int value= arr[k-1];
//        for (int i=k-1; i<n; i++)
//        {
//            if(value == arr[i]) continue;
//            else
//        }
//        System.out.println(advanceed_number);
