import java.util.Scanner;

public class ChartRoom {
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
              // 다음 인덱스에 해당하는 값을 대입해서 피봇 초기화
              lookingFor= hello[index];
          }
        }  
      System.out.println("NO");
    }
}
