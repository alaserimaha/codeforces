/******************************************************************************
160A - A. Twins

*******************************************************************************/

public class Main
{
	public static void main(String[] args) {
	    public static void main(String argv[]) {
		Scanner sc=new Scanner(System.in);
		int a=sc.nextInt();
		String bla=sc.nextLine();
		int[]b=new int[a];
		int total=0;
		int count=0;
		
		int num=0;
		
		for(int i =0;i<b.length;i++) {
			b[i]=sc.nextInt();
			total=total+b[i];
		
		}
		Arrays.sort(b);
		for(int i =b.length-1 ;i>=0;i--) {
			count=count+b[i];
			num++;
			if((total-count)<count) {
				break;
			}
			
		}
		System.out.println(num)
	}
}
