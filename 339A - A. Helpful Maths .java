/******************************************************************************
339A - A. Helpful Maths

*******************************************************************************/

public class Main
{
public static void main(String[] args) {
		Scanner a = new Scanner(System.in);
		String a1=a.nextLine();
		int b []= new int[(a1.length()/2+1)];
		int count=0;
		for(int i =0 ; i < b.length;i++) {
			b[i]=Character.getNumericValue(a1.charAt(count));
			count=count+2;
		}
		Arrays.sort(b);
		
		String new1="";
		for(int i =0 ; i < b.length;i++)
			new1=new1+b[i]+"+";
 
 
			System.out.println(new1.substring(0, new1.length()-1));

 
}
}
