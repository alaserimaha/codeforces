/******************************************************************************
110A - A. Nearly Lucky Number

*******************************************************************************/

public class Main
{
		public static void main(String argv[]) {
		 Scanner in = new Scanner(System.in);
		 String s=in.nextLine();
		 String res;
		 int count=0;
 
		 
			 for(int i = 0; i <s.length() ; i++) {
				 if(s.charAt(i)=='4' || s.charAt(i)=='7') {
					count++; 
				 }}
			 if(count ==4 || count ==7) {
				 res="YES";
			 }else {
				 res="NO";
			 }
		 
		
		 System.out.println(res);
 
	
	}
}
