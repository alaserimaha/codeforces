/******************************************************************************
677A - A. Vanya and Fence

*******************************************************************************/

public class Main
{
		public static void main(String argv[]) {
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt();
		int b = sc.nextInt();
		String c= sc.nextLine();
		int [] arr= new int [a];
		int count=0;
		
		for (int i =0; i < arr.length;i++) {
			arr[i]=sc.nextInt();
		}
		
		for (int i =0; i < arr.length;i++) {
		      if(arr[i]<=b) {
		    	  count++;
		      }else if(arr[i]>b) {
		    	  count=count+2; 
 
		      }
		}
		System.out.println(count);
		
 
		
	      
}
}
