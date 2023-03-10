/******************************************************************************

785A - A. Anton and Polyhedrons

*******************************************************************************/

public class Main
{
	public static void main(String[] args) {
Scanner sc=new Scanner(System.in);
		int a=sc.nextInt();
		String bla=sc.nextLine();
		String arr[]=new String[a];
		int count=0;
		
		for(int i=0;i<a;i++) {
			arr[i]=sc.nextLine();
			if (arr[i].equals("Tetrahedron")) {
				count=count+4;
			}else if (arr[i].equals("Cube")) {
				count=count+6;
			}else if (arr[i].equals("Octahedron")) {
				count=count+8;
			}else if (arr[i].equals("Dodecahedron")) {
				count=count+12;
			}else if (arr[i].equals("Icosahedron")) {
				count=count+20;
			}
			
 
		}
		
		System.out.println(count);	
		}
}
