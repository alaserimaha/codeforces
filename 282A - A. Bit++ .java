/******************************************************************************
282A - A. Bit++

*******************************************************************************/

public class Main
{
public static void main(String[] args) {
		int count=0;
		Scanner a = new Scanner(System.in);
		int n= a.nextInt();
		String[] b= new String [n+1];
		for(int i = 0 ; i <n+1 ; i++) {
			b[i]=a.nextLine();
			
			if ( b[i].equals("++x")|| b[i].equals("+x+")|| b[i].equals("x++")||
					 b[i].equals("++X")|| b[i].equals("+X+")|| b[i].equals("X++"))
				count++;
			else if( b[i].equals("--x")|| b[i].equals("-x-")|| b[i].equals("x--")||
					 b[i].equals("--X")|| b[i].equals("-X-")|| b[i].equals("X--"))
				count--;				
				
		}
	
		System.out.println(count);
			}
}
