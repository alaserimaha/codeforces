/******************************************************************************

705A - A. Hulk

*******************************************************************************/

public class Main
{
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int a=sc.nextInt();
				
		String love="I love that ";
		String hate="I hate that ";
		String love_final="I love it ";
		String hate_final="I hate it ";
		String rsult="";
 
		for(int i=1;i<=a;i++) {
			if(i==a) {
				if(i%2==0) {
					rsult=rsult+love_final;
				}else if(i%2==1) {
					rsult=rsult+hate_final;
 
				}
			}else {
				if(i%2==0) {
					rsult=rsult+love;
				}else if(i%2==1) {
					rsult=rsult+hate;
 
				}
			}}
	
 
			System.out.println(rsult);
			
	}
}
