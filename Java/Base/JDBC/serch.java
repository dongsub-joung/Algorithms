package books;

public class serch {


	public class Method{
		/*
		public static void getName() {
			input�� string �޾ƿ�.
			return bookName;
		}
		*/
		
		//�Է¹��� å �̸��� DB���� �˻� �� ����Ǿ� �ִ� ���� ��ȯ
		public static void bookSerch() {
			//user�κ��� å �̸��� �޾ƿ�.
			String bookName= getName();
			//SQL
			String sql= sb.append("select*from books where book_title=\""+ bookName + "\";").toString();
			stmt.execute(sql);
			
			
		}
	}
	
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}
}