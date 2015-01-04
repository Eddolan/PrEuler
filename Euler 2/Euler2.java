
public class Euler2 {
	public static void main(String[] args) {
		System.out.println(fibonacci());
	}
	
	private static int fibonacci() {
		int n1 = 1;
		int n2 = 2;
		int total = 0;
		while (n2 < 4000000) {
			if (n2 % 2 == 0) total += n2;
			int temp = n2;
			n2 += n1;
			n1 = temp;
		}
		return total;
	}
}
