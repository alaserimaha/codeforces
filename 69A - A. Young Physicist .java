/******************************************************************************
69A - A. Young Physicist

*******************************************************************************/

public class Main
{
		public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int t = in.nextInt();
		int[][] mat = new int[t][3];
		int[] sums = new int[3];
		for (int i = 0; i < t; i++) {
			for (int j = 0; j < 3; j++) {
				mat[i][j] = in.nextInt();
				sums[j] += mat[i][j];
			}
		}		
		if (sums[0] == 0 && sums[1] == 0 && sums[2] == 0)
			System.out.println("YES");
		else
			System.out.println("NO");
		in.close();
	}
}
