/******************************************************************************

                            Online Java Compiler.
                Code, Compile, Run and Debug java program online.
Write your code in this editor and press "Run" button to execute it.

*******************************************************************************/

public class Main
{
	public static void main(String[] args) {
		Scanner a = new Scanner(System.in);
		int a1= a.nextInt();
		if(a1 <101)
			if(a1%2==0 && a1!=2)
				System.out.println("YES");
			else {
				System.out.println("NO");
			}
}
