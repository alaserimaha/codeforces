/******************************************************************************
158A - A. Next Round

*******************************************************************************/

public class Main
{
	public static void main(String[] args) {
		int count=0;
		Scanner a = new Scanner(System.in);
		int n= a.nextInt();
		int k= a.nextInt();
		int [] b = new int[n];
		for(int i=0; i < b.length ; i++) {
			b[i]=a.nextInt();
			 }
		for (int i = 0 ; i < b.length ;i++) 
			if (b[i]>0 && b[i]>= b[k-1]) {
			count++;}
			
		System.out.println(count);
			}
}
