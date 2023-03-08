/******************************************************************************
112A - A. Petya and Strings

*******************************************************************************/

public class Main
{
public static void main(String[] args) {
		Scanner a = new Scanner(System.in);
		String a1=a.nextLine().toLowerCase();
		String a2=a.nextLine().toLowerCase();
					
		if(a1.compareTo(a2)==0)
			System.out.println(0);
		else if(a1.compareTo(a2)>0)
			System.out.println(1);
		else {
			System.out.println(-1);
 
		}
 
}
}
