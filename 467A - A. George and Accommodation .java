/******************************************************************************

467A - A. George and Accommodation

*******************************************************************************/

public class Main
{
	public static void main(String[] args) {
	    Scanner sc=new Scanner(System.in);
		int a=sc.nextInt();
		String bla=sc.nextLine();
		
		int[][]b=new int[a][2];
		int total=0;
		int count=0;
		
		int num=0;
 
		for(int i =0;i<b.length;i++) {
			for(int j =0;j<b[0].length;j++) {
			b[i][j]=sc.nextInt();}
			if(b[i][0]+1<b[i][1]) {
				count++;
			}
			bla=sc.nextLine();
		}
		
		System.out.println(count);
 
	}
}
