package ex1;
	//달팽이 배열 입력받고 출력하기
public class triangle_arrangement {
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		int triangle[][] = new int[6][6];
		
		int R =0; //행 변수
		int C =-1; //열변수 , 스위치 변수 고려
		
		int N =0; // 배열에 넣을 값=배열 값
		int K = 5; // 데이터 입력 N의 반복 변수
		int M;	//반복 변수
		
		int S = 1; //스위치 변수
		
		while(true) {
			for(M=1; M<=K; M++) {	//M에서 K까지 반복
				N+=1;		//N=N+1  
				C=C+S;	//행 고정 열의 변화 
				triangle[R][C]=N;	//
			}
			K-=1;		//5,44,33,22,11
			if(K==0) break;
			
			for(M=1;M<=K;M++) {
				N+=1;
				R=R+S;	//행 변화 열 고정
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
