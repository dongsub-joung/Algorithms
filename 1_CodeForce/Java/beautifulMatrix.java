package code;
// https://moatazmshawky.wordpress.com/2016/06/05/263a-beautiful-matrix-java/

import java.io.IOException;
import java.util.Scanner;

public class beautifulMatrix{
    public static void main(String[] args) throws IOException {
        try
        {
            Scanner sc= new Scanner(System.in);
    //      init value
            int MAX_SIZE= 5;
            char [][] matrix= new char[MAX_SIZE][MAX_SIZE];

    //      5* 1 line
            for (int i=0; i<MAX_SIZE; i++)
            {
                matrix[i]= sc.next().replaceAll(" ", "").toCharArray();
            }

    //      find '1' index [][]
            int R= -1, C= -1;
            for (int i=0; i<MAX_SIZE; i++)
            {
                for (int j=0; j<MAX_SIZE; j++)
                {
                    if (matrix[i][j] == '1')
                    {
                        R= i;
                        C= j;
                        break;
                    }
                }
            }

            int moves= Math.abs(R-2)+Math.abs(C-2);
            System.out.println(moves);

            sc.close();
        } catch (Exception e)
        {
            e.printStackTrace();
        }
    }
}

//pseudo code
//  find '1' index [][] <- [2][2]
//  절대 값