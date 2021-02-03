// https://kookyungmin.github.io/language/2018/05/22/java_06/

package test;

public class test
{
    public static void main(String[] args) {
        System.out.println(args.length);
        for (int i=0; i<args.length; i++)
        {
            System.out.println(args[i]);
        }
    }
}

// case3
//    public static void main(String[] args) {
//        String[] arr= new String[]{"넷z", "둘d", "셋f", "하나"};
//        for(String str:arr)
//        {
//            System.out.println(str);
//            char[] temp= str.toCharArray();
//            System.out.println(temp[0]);
//        }
//    }
//    넷z
//            넷
//    둘d
//            둘
//    셋f
//            셋
//    하나
//            하

// case 2
//    public static void main(String[] args) {
//        String[] arr= new String[]{"넷", "둘", "셋", "하나"};
//        for(int i=0; i<4; i++)
//        {
//            System.out.println(arr[i]);
//        }
//    }
//  넷
//  둘
//  셋
//  하나


// case 1
//    public static void main(String[] args) {
//        String arr = new String();
//
//        arr_1= "넷둘셋하나";
//        arr_2= "넷"+"둘"+"셋"+"하나";

//        System.out.println(arr_1.charAt(i));
//        System.out.println(arr_2.charAt(i));
//    }
//            넷
//            둘
//            셋
//            하
