package books;

import java.sql.*;

public class JDBC {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		String url= "jdbc:mysql://localhost:3306/first?serverTimezone=UTC";
		String user= "root";
		String pass= "111111";
		
		Connection conn = null;
		Statement stmt = null;
		
		try {
			//JDBC ����̹� �ε�
			Class.forName("com.mysql.cj.jdbc.Driver");
			
			//MySQL���� ���� �۾��� ���� Connection ��ü ����	
			conn = DriverManager.getConnection(url, user, pass);
			System.out.println("����"+ conn);
			
			//DB������ SQL query���� �����ϰ�, DB�� ó���� ����� �ٽ� �ڹ����α׷������� ������ �� �ֵ��� ���� ��ü�̴�.
			//conn ��ü�κ��� Statement ��ü ȹ��
			stmt = conn.createStatement();
			
			//query �����
			
			StringBuilder sb= new StringBuilder();
			String sql= sb.append("SELECT*FROM books").toString();
			
			//query�� ������
			stmt.execute(sql);	
		}
		
		catch (ClassNotFoundException e) {
			System.out.println("����̹� �˻� ����!");
			e.printStackTrace();
		}
		
		catch (SQLException e) {
			e.printStackTrace();
		}
	
		finally{
	            try{
	                //�ڿ� ����
	                if(conn != null && !conn.isClosed())
	                    conn.close();
	            } 
	            catch(SQLException e){
	                e.printStackTrace();
	            }
	       }
	}
}
