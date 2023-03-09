/******************************************************************************

1030A - A. In Search of an Easy Problem

*******************************************************************************/

public class Main
{
	public static void main(String[] args) {
	    Scanner sc=new Scanner(System.in);
		int a=sc.nextInt();
		String bla=sc.nextLine();
		
		int[]b=new int[a];
	    boolean re=true;
		int num=0;
 
		for(int i =0;i<b.length;i++) {
			b[i]=sc.nextInt();
			if(b[i]==1) {
				re=false;
				}
		}
		if(re==true) {
			System.out.println("EASY");
 
		}else {
			System.out.println("HARD");
 
		}
	}
}
