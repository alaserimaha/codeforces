/******************************************************************************

200B - B. Drinks

*******************************************************************************/

public class Main
{
	public static void main(String[] args) {
	   Scanner sc=new Scanner(System.in);
		int a = sc.nextInt();
		int arr[]=new int[a];
		double temp=0;
		String bla=sc.nextLine();
		
		double total=0;
		
		for(int i=0;i<a;i++) {
			arr[i]=sc.nextInt();
			temp=(double)arr[i]/100;
			total=total+temp;
		}
		
 
			System.out.println((double)(total*100)/a);

	}
}
