/******************************************************************************
59A - A. Word

*******************************************************************************/

public class Main
{
		public static void main(String args[]) { 
			Scanner a= new Scanner(System.in);
			String b= a.nextLine();
			int l =0;
			int u=0;
			for(int i =0; i < b.length();i++) {
            if(Character.isLowerCase(b.charAt(i))) {
            	l++;
            }else if (Character.isUpperCase(b.charAt(i))){
            	u++;
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
