/******************************************************************************

230A - A. Dragons

*******************************************************************************/

public class Main
{
	public static void main(String[] args) {
Scanner sc=new Scanner(System.in);
		int s =sc.nextInt();
		int a=sc.nextInt();
		String bla=sc.nextLine();
		int arr[][]=new int[a][2];
		String re="YES";
 
		for(int i=0;i<a;i++) {
			arr[i][0]=sc.nextInt();
			arr[i][1]=sc.nextInt();
			bla=sc.nextLine();
		}
		Arrays.sort(arr, Comparator.comparingDouble(o -> o[0]));
 
		
		
		for(int i=0;i<a;i++) {
			if(s>arr[i][0]) {
				s=s+arr[i][1];
			}else {
				re="NO";
				break;
			}
		}
		System.out.println(re);
		}
}
