package book;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class test {

	public static void main(String[] args) {
		
		String url= "jdbc:mysql://localhost:3306/first?serverTimezone=UTC";
		String user= "root";
		String pass= "111111";
		
		Connection conn;
		
		try {
			Class.forName("com.mysql.cj.jdbc.Driver");
			System.out.println("����̹� �˻� ����!");
			conn = DriverManager.getConnection(url, user, pass);
			System.out.println("���� ����"+conn);
		} catch (ClassNotFoundException e) {
			System.out.println("����̹� �˻� ����!");
			e.printStackTrace();
		}
		
		catch (SQLException e) {
			e.printStackTrace();
		}
	}
}