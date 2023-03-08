/******************************************************************************
266B - B. Queue at the School

*******************************************************************************/

public class Main
{
		public static void main(String argv[]) {
		 Scanner in = new Scanner(System.in);
		 int a = in.nextInt();
		 int b = in.nextInt();
		 String f= in.nextLine();
 
		 String c= in.nextLine();
		 
		 char d[]=new char [a];
		 
		 for (int i =0 ; i<d.length ;i++) {
			 
			 d[i]=c.charAt(i);
		 }
		 
         for(int j=0; j <b ; j++) {
		 for (int i =0 ; i<(d.length-1) ;i++) {
			 if (d[i]=='B'&& d[1+i]=='G') {
				d[i]='G'; 
				d[i+1]='B'; 
				i++;
			 }
			 
			
		 }}
 for (int i =0 ; i<d.length ;i++) {
			 
     System.out.print(d[i]);
		 }
 
	
	}
}
