/******************************************************************************

1335A - A. Candies and Two Sisters

*******************************************************************************/

public class Main
{
	public static void main(String[] args) {
Scanner sc=new Scanner(System.in);
		int a=sc.nextInt();
		String bla=sc.nextLine();
		int arr[]=new int[a];
		int re []=new int[a];
		int count=0;
		int num1;
		int num2;
		
		for(int i=0;i<a;i++) {
			arr[i]=sc.nextInt();
		}
		for(int i=0;i<a;i++) {
			count=0;
			if(arr[i]%2==0) {
				count=arr[i]/2-1;
			}else {
				count=arr[i]/2;
			}
			re[i]=count;
		}
		for(int i=0;i<a;i++) {
			System.out.println(re[i]);	
		}
		}
}
