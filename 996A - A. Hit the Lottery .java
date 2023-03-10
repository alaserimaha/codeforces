/******************************************************************************

996A - A. Hit the Lottery

*******************************************************************************/

public class Main
{
	public static void main(String[] args) {
Scanner sc=new Scanner(System.in);
		int a=sc.nextInt();
		int temp;
		int count=0;
		
		temp=a/100;
		a=a-(100*temp);
		count=count+temp;
		
		temp=a/20;
		a=a-(20*temp);
		count=count+temp;
		
		temp=a/10;
		a=a-(10*temp);
		count=count+temp;
 
		
		temp=a/5;
		a=a-(5*temp);
		count=count+temp;
 
		
		temp=a/1;
		a=a-(1*temp);
		count=count+temp;
 
		System.out.println(count);
		}
}
