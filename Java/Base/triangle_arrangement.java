package ex1;
	//������ �迭 �Է¹ް� ����ϱ�
public class triangle_arrangement {
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		int triangle[][] = new int[6][6];
		
		int R =0; //�� ����
		int C =-1; //������ , ����ġ ���� ���
		
		int N =0; // �迭�� ���� ��=�迭 ��
		int K = 5; // ������ �Է� N�� �ݺ� ����
		int M;	//�ݺ� ����
		
		int S = 1; //����ġ ����
		
		while(true) {
			for(M=1; M<=K; M++) {	//M���� K���� �ݺ�
				N+=1;		//N=N+1  
				C=C+S;	//�� ���� ���� ��ȭ 
				triangle[R][C]=N;	//
			}
			K-=1;		//5,44,33,22,11
			if(K==0) break;
			
			for(M=1;M<=K;M++) {
				N+=1;
				R=R+S;	//�� ��ȭ �� ����
				triangle[R][C]=N;
			}
			S=S*(-1); 	
		}				
		
		for(R=0;R<5;R++) {
			for(C=0;C<5;C++)
				System.out.println(triangle[R][C]+"\t");
			System.out.println(); 
		}
	}

}
