/******************************************************************************

136A - A. Presents

*******************************************************************************/

public class Main
{
	public static void main(String[] args) {
	   Scanner sc=new Scanner(System.in);
		int a=sc.nextInt();
		String bla=sc.nextLine();
		
		int[]b=new int[a];
		int[]c=new int[a];
 
	    boolean re=true;
		int num=0;
 
		for(int i =0;i<b.length;i++) {
			b[i]=sc.nextInt();
		
				}
 
		for(int i =0;i<b.length;i++) {
				c[b[i]-1]=1+i;
		
				}
		for(int i =0;i<c.length;i++) {
			System.out.print(c[i]+" ");
		
				}
	

	}
}
