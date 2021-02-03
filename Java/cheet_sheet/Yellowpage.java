package yellowpage;

// https://blog.naver.com/PostView.nhn?blogId=editinside&logNo=220784778525&categoryNo=15&parentCategoryNo=0&viewDate=&currentPage=1&postListTopCurrentPage=&from=menu&userTopListOpen=true&userTopListCount=5&userTopListManageOpen=false&userTopListCurrentPage=1

import java.util.HashMap;
import java.util.Iterator;
import java.util.Scanner;
import java.util.Set;


class Phone
{
    Scanner sc= new Scanner(System.in);
    String name, address;
    int number;

    Phone()
    {
        System.out.println("name>>");
        this.name= sc.next();
        System.out.println("address>>");
        this.address= sc.next();
        System.out.println("number>>");
        this.number= sc.nextInt();
    }

    @Override
    public String toString()
    {
        return "#name=" + name  + ", address=" + address + ",number= " + number + "]";
    }
}

public class Yellowpage
{
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        HashMap<String, Phone> map= new HashMap<String, Phone>();

        System.out.println("전화번호 관리 프로그램을 시작합니다. 파일로 저장하지 않습니다.");

        while (true)
        {
            System.out.println("Insert:0 / Delete:1 / Search:2 / View:3 / exit:4 >>");
            int a= sc.nextInt();
            switch(a)
            {
                case 0:
                    Phone ph= new Phone();
                    map.put(ph.name, ph); break;
                case 1:
                    System.out.println("name>>");
                    String del_name= sc.next();
                    try
                    {
                        map.remove(del_name);
                        System.out.println("Deleted "+del_name);
                    } catch (Exception e)
                    {
                        System.out.println("Not exist ["+del_name+"]");
                    } break;
                case 2:
                    System.out.println("name>>");
                    String get_name= sc.next();
                    System.out.println(map.get(get_name)); break;
                case 3:
                    Set<String> s= map.keySet();
                    Iterator<String> it= s.iterator();
                    while (it.hasNext())
                    {
                        String str= it.next();
                        System.out.println(map.get(str));
                    } break;
                case 4:
                    System.out.println("Shutdown");
                    System.exit(1);
            }
        }
    }
}
