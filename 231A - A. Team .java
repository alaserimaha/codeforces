/******************************************************************************
231A - A. Team
*******************************************************************************/

public class Main
{
	public static void main(String[] args) {
		int sum=0;
		int count=0;
		Scanner a = new Scanner(System.in);
		int a1= a.nextInt();
		int [][] b = new int[a1][3];
		for(int i=0; i < b.length ; i++) {
			for(int j=0;j<b[0].length ;j++) {
				b[i][j]=a.nextInt();
				sum=sum+b[i][j];}
			if(sum>1)
				count++;
			sum=0;
			
		
		}
		System.out.println(count);
			}
}
