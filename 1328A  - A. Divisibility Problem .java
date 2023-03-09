/******************************************************************************

1328A  - A. Divisibility Problem


*******************************************************************************/

public class Main
{
	public static void main(String[] args) {
	  Scanner sc=new Scanner(System.in);
		
		int a=sc.nextInt();
		int num1;
		int num2;
		int count=0;
		int re[]=new int[a];
		int div1;
		int div2;
		
		
		
		for(int i=0,j=0;i<a;i++) {
			count=0;
			num1=sc.nextInt();
			num2=sc.nextInt();
			while (true){
				if (num1%num2==0) {
					re[j]=count;
					j++;
					break;
				}else {
					div1 =num1/num2+1;
					count= (div1*num2)-num1;
					re[j]=count;
					j++;
					break;
				}}
		
			}
			
			for (int i=0; i<a;i++)
			System.out.println(re[i]);
 

	}
}
