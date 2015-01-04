
public class Euler5 {
	public static void main(String[] args) {
		int max = 20;
		int currLcm = 2;
		for (int i = 3; i <= max; i++) {
			currLcm = lcm(currLcm, i);
			System.out.println(currLcm + " " + i);
		}
		//System.out.println(currLcm);
	}
	
	private static int lcm(int a, int b) {
		return ((a * b)/gcd(a,b));
	}
	
	private static int gcd(int a, int b) {
		if (b == 0) return a;
		return gcd(b, a % b );
	}
}
