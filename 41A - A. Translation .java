/******************************************************************************
41A - A. Translation


*******************************************************************************/

public class Main
{
		public static void main(String argv[]) {
		Scanner sc = new Scanner(System.in);
	    String str1 = sc.nextLine();
	    String str2 = sc.nextLine();
	    String str3="";
	    
	    for(int i =str1.length()-1 ; i>=0;i--) {
	    	str3=str3+str1.charAt(i);
	    	
	    }
	    if(str3.equals(str2)) {
		      System.out.println("YES");
 
	    }else {
		      System.out.println("NO");
 
	    }
 
 
 
	      
}
}
