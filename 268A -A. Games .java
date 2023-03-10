/******************************************************************************

268A -A. Games

*******************************************************************************/

public class Main
{
	public static void main(String[] args) {
Scanner sc=new Scanner(System.in);
		int a=sc.nextInt();
		String bla=sc.nextLine();
		int arr[][]=new int[a][2];
		int count=0;
 
		for(int i=0;i<a;i++) {
			arr[i][0]=sc.nextInt();
			arr[i][1]=sc.nextInt();
			bla=sc.nextLine();
			}
			
			for (int i=0; i<a;i++)
				for (int j=0 ; j<a;j++) {
					if (arr[i][0]==arr[j][1]) {
						count++;
					}
				}
			System.out.println(count);	}
}
