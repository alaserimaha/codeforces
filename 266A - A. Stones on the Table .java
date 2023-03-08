/******************************************************************************
266A - A. Stones on the Table

*******************************************************************************/

public class Main
{
		public static void main(String[] args) {
		Scanner a = new Scanner(System.in);
		int n= a.nextInt();
		int count =0;
		char a1[]=new char[n];;
		String a2=a.next();;
		int temp=1;
 
		for(int i=0;i<a1.length;i++)
			a1[i]= a2.charAt(i);
		for(int i=0;i<a1.length-1;i++) {
			if(a1[i]==a1[temp])
				count++;
		temp++;}
 
			System.out.println(count);
			
}
}
