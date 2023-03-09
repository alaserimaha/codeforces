/******************************************************************************

318A - A. Even Odds

*******************************************************************************/

public class Main
{
	public static void main(String[] args) {
	   Scanner sc=new Scanner(System.in);
		long num1=sc.nextLong();
		long num2=sc.nextLong();
		long hafe=0;
		long a=1;
		
		if(num1%2==0) {
			hafe=num1/2;
		}else if(num1%2==1) {
			hafe=num1/2 +1;
		}
		
		
		if(num2<=hafe) {
			a=a+(2*(num2-1));
		}else if(num2>hafe) {
			num2=num2-hafe;
			a=0;
			a=a+(2*(num2));
		}
		
		System.out.print(a);

	}
}
