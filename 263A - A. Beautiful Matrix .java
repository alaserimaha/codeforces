/******************************************************************************
263A - A. Beautiful Matrix

*******************************************************************************/

public class Main
{
public static void main(String args[]) {
		Scanner sc=new Scanner(System.in);
		int a[][]=new int[5][5];
		int count=0;
		String bla;
		int c=0;
		int r=0;
		
		for(int i=0;i<5;i++) {
			for(int j=0;j<5;j++) {
			a[i][j]= sc.nextInt();
			if(a[i][j]==1) {
				c=i;
				r=j;
			}
				}
			bla=sc.nextLine();
 
			}
		while(true){
			if(c>2) {
				c--;
				count++;
			}
			if(c<2) {
				c++;
				count++;
			}
			if(r>2) {
				r--;
				count++;
			}
			if(r<2) {
				r++;
				count++;
			}
			if(r==2&&c==2) {
				break;
			}
			
			
		}
			
	
		
		
 
			System.out.println(count);
 
		
 
 
 
		
		
}
}
