/******************************************************************************
116A - A. Tram

*******************************************************************************/

public class Main
{
		public static void main(String args[]) {
		Scanner sc=new Scanner(System.in);
		
		int a=sc.nextInt();
		int arr[][]=new int[a][2];
		int count=0;
		int max=0;
		String bla="";
		
		for(int i=0;i<a;i++) {
			for(int j=0;j<2;j++) {
			arr[i][j]= sc.nextInt();}
			bla=sc.nextLine();
			}
		
		for(int i=0;i<a;i++) {
				count=count-arr[i][0];
				count=count+arr[i][1];
				
				if(count>=max) {
					max=count;
				
			}
			}

			System.out.println(max);
		
}
}
