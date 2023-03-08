/******************************************************************************
617A - A. Elephant

*******************************************************************************/

public class Main
{
		public static void main(String args[]) { 
			Scanner a= new Scanner(System.in);
			int dis = a.nextInt();
			int count=0;
			int total=0;
			if (dis <6) {
				System.out.println(1);
			}
			else {
				if(dis%5==0) {
					System.out.println(dis/5);					
				}
				else {
					for (int i =0 ; dis%5!=0 ;i++) {
						dis--;
						count++;
					}
					total = dis/5 +1;
					System.out.println(total);					
				}
				
			}
	}
}
