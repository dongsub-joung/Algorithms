package ex1;

public class numroll2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int sum = 0;
		int n=1;
		
		while(true) {
			sum +=n;
			n=n+1;
			if(n>100) break;	
		}
		System.out.println(sum);
	}

}
