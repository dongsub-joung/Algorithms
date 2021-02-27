import java.util.Scanner;

public class Word {
    public static void main(String[] args) {

        Scanner sc= new Scanner(System.in);
        String inputed= sc.next();
        String toLower= inputed.toLowerCase();
        String toUpper= inputed.toUpperCase();

//        Compare
        int cnt_low=0, cnt_upper=0;
        char[] arr_inputed= inputed.toCharArray();
        for (char value : arr_inputed)
        {
            if (value >= 65 && value <= 90) cnt_upper++;
            else if (value >= 97 && value <= 122) cnt_low++;
        }

        if (cnt_low >= cnt_upper) System.out.println(toLower);
        else System.out.println(toUpper);
    }
}
