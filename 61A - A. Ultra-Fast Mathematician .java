/******************************************************************************

61A - A. Ultra-Fast Mathematician

*******************************************************************************/

public class Main
{
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		String a=sc.nextLine();
		String b=sc.nextLine();
		String c="";
 
		for(int i=0;i<a.length();i++) {
			if(a.charAt(i)==b.charAt(i)) {
				c=c+'0';
			}else {
				c=c+'1';
 
			}
			
		}
		
 
			System.out.println(c);
	}
}
