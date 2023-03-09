/******************************************************************************

405A  - A. Gravity Flip


*******************************************************************************/

public class Main
{
	public static void main(String[] args) {
	   Scanner sc=new Scanner(System.in);
		int a= sc.nextInt();
		String bla=sc.nextLine();
		int arr[]= new int[a];
		
		for(int i=0;i<a;i++) {
			arr[i]= sc.nextInt();
 
		}
		Arrays.sort(arr);
		for(int i=0;i<a;i++) {
			System.out.print(arr[i]+" ");
 
		}

	}
}
