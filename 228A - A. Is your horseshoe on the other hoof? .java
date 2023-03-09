/******************************************************************************

228A - A. Is your horseshoe on the other hoof?

*******************************************************************************/

public class Main
{
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int a[]= new int[4];
		for(int i=0;i<4;i++) {
			a[i]= sc.nextInt();
 
		}
		Arrays.sort(a);
		int count = 0 ;
		
		for(int i=0;i<4-1;i++) {
			if(i==0) {
				if (a[i]==a[1+i]) {
					count++;
				}else {
					count=count+2;
				}}else {	
			if (a[i]==a[1+i]) {
			}else {
				count++;
			}}}
 
			System.out.println(4-count);
			
	}
}
