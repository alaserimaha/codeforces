/******************************************************************************
71A - A. Way Too Long Words
*******************************************************************************/

public class Main
{
	public static void main(String[] args) {
		Scanner a = new Scanner(System.in);
		int a1= a.nextInt();
		String word1;
		String total="";
		if(a1 <101)
			for(int i = 1 ; i<= a1+1 ; i++) {
				word1=a.nextLine();
				if (word1.length()<11) {
					if(total.length()==0)
					total=word1+"\n";
					else {
						total=total+"\n"+word1;
					}
				}
				else if (word1.length() < 101) {
					word1=word1.charAt(0)+""+(word1.length()-2) +""+ word1.charAt(word1.length()-1);
					if (word1.length()<11) {
						if(total.length()==0)
						total=word1+"\n";
						else {
							total=total+"\n"+word1;
						}
					}					}
			}
		System.out.println(total);
 
	}
}
