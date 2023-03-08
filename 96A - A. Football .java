/******************************************************************************
96A - A. Football

*******************************************************************************/

public class Main
{
		public static void main(String[] args) {
		Scanner a= new Scanner(System.in);
	String n = a.nextLine();
	int arr[]=new int[n.length()];
	for(int i = 0 ; i < arr.length;i++)
		arr[i]=n.charAt(i);
	int fin=0;
	int count=0;
	int temp=1;
	for(int i = 0 ; i < arr.length-1;i++ , temp++)
		if(arr[i]==arr[temp]) {
 
			count++;
 
			if(count>=6)
				fin++;
		}
			else {
 
				count=0;
 
			}
 
		
	
	if(fin>=1)
	System.out.println("YES");
	else {
		
	
	System.out.println("NO");
 
	}
	}
		if(l>u) {
		b=	b.toLowerCase();
		}else if(u>l) {
			b=b.toUpperCase();
		}else {
			b=b.toLowerCase();
		}
		
		System.out.println(b);
			
			
		}
}
