/******************************************************************************
977A - A. Wrong Subtraction

*******************************************************************************/

public class Main
{
		public static void main(String argv[]) {
		 Scanner in = new Scanner(System.in);
		 int a=in.nextInt();
		 int b=in.nextInt();
		 int res=a;
		 
		 for(;b>0;b--) {
			 if (res%10==0) {
				 res=(res/10);
			 }else {
				 res=(res-1);
 
			 }
		 }
		 System.out.println(res);
 
	
	}
}
