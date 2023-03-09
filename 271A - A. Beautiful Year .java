/******************************************************************************
271A - A. Beautiful Year

*******************************************************************************/

public class Main
{
	public static void main(String[] args) {
	    	Scanner sc = new Scanner(System.in);
		int a = sc.nextInt()+1;
		String b =String.valueOf(a);
		boolean re=false;
		char charArray[] = b.toCharArray();
	    Arrays.sort(charArray);
        b = new String(charArray);
 
 
		
		
		for(int j=1; re==false ; a++ ,b =String.valueOf(a),charArray = b.toCharArray(),Arrays.sort(charArray),b = new String(charArray))
		for (int i = 0; i < b.length()-1; i++)
		{ if (b.charAt(i)==b.charAt(1+i)) 
		{ 
			re=false;
			break;}
		else {
				re=true;
 
			}
		} 	
 
	      System.out.println(a-1);
	}
}
