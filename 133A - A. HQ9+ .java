/******************************************************************************

133A - A. HQ9+

*******************************************************************************/

public class Main
{
Scanner sc=new Scanner(System.in);
		String a=sc.nextLine();
	
	    boolean re=false;
 
		for(int i =0;i<a.length();i++) {
			if(a.charAt(i)=='H'||a.charAt(i)=='Q'||a.charAt(i)=='9') {
				re=true;
				break;
			}
		
				}
 
		
		if(re==true) {
			System.out.print("YES");
 
		}else {
			System.out.print("NO");
 
		}

	}
}
