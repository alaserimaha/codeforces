/******************************************************************************
118A - A. String Task

*******************************************************************************/

public class Main
{
	public static void main(String[] args) {
		Scanner a = new Scanner(System.in);
		String a1=a.nextLine().toLowerCase();
		String a2=".";
		boolean b=false;
					
		
		for(int i =0 ; i < a1.length();i++)
					if(a1.charAt(i)=='a'||a1.charAt(i)=='e'||a1.charAt(i)=='i'||a1.charAt(i)=='u'||
							a1.charAt(i)=='o'||a1.charAt(i)=='y') {
						if(b==false) {
						
						b=true;}
						else {
							continue;
						}
					}else {
						a2=a2+a1.charAt(i)+".";
						b=false;
 
						
					}
		if(a2.charAt(a2.length()-1)=='.')
			System.out.println(a2.substring(0, a2.length()-1));
		else
			System.out.println(a2);
 
		
 
}
}
