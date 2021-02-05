import java.util.Scanner;

public class WayTooLongWords
{
  public static void main(String[] args) {
    Scanner sc= new Scanner(System.in);
    String inputed_string;
    
    for(int i=sc.nextInt(); i>0; i--)
    {
      inputed_string= sc.next();
      int len= inputed_string.length();
      if(len > 10)
      {
        int adjust_num= 2;

        char FIRST_CHAR= inputed_string.charAt(0);
        String len_char= Integer.toString(len-adjust_num);
        char RAST_CHAR= inputed_string.charAt(len-1);
        String output= FIRST_CHAR + len_char + RAST_CHAR; 
        System.out.println(output);
      }
      else System.out.println(inputed_string); 
    }
  }
}


// 문제를 잘못 이해해서 만든 것
// 반복 횟수, "word", 이후에 오는 단어를 축약하는 것으로 받아드림.

// public static void main(String[] args) {
//   Scanner sc= new Scanner(System.in);
//   int count= sc.nextInt();
//   String output;
//   for(int i=0; i<count; i++)
//   {
//     Scanner word= new Scanner(System.in);
//     if(i == 0) output= word.nextLine();
//     else
//     {
//       output= invertedString(word.nextLine());
//     } 
//     System.out.println(output);
//   }
// }

// public static String invertedString(String str)
// {
//   int len= str.length();
//   int adjust_num= 2;

//   char FIRST_CHAR= str.charAt(0);
//   String len_char= Integer.toString(len-adjust_num);
//   char RAST_CHAR= str.charAt(len-1);
//   String result= FIRST_CHAR + len_char + RAST_CHAR; 
//   return result;
// }