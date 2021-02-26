import java.util.Scanner;

public class ChartRoom {

    public void answer01()
    {
        Scanner in = new Scanner(System.in);
        String input = in.nextLine();

        String matcher = "hello";

        int count = 0;

        for(int i=0;i<input.length();i++){
            if(count == matcher.length())
                break;

            if(input.charAt(i) == matcher.charAt(count))
                count++;
        }

        if(count>=5)
            System.out.println("YES");
        else
            System.out.println("NO");
    }

    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        String str= sc.next();

        Character[] hello= {'h', 'e', 'l', 'l', 'o'};
        int index= 0;
        char lookingFor= hello[index];

        for (char c : str.toCharArray())
        {
            if (c == lookingFor && index == 4)
            {
                System.out.println("YES");
                return;
            }
            else if (c == lookingFor)
            {
                index++;
                lookingFor= hello[index];
            }
        }
        System.out.println("NO");
    }
}

