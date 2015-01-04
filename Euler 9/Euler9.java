public class Euler9 {
	public static void main(String[] args) {
		System.out.print(pythTriplet());
		System.out.println(".");
	}
	
	public static int pythTriplet() {
		for (int a = 500; a > 0; a--) {
			for (int b = 500; b > 0; b--) {
				double c = Math.sqrt(Math.pow(a, 2) + Math.pow(b, 2));
				if (a + b + c == 1000) {
					System.out.println("A is " + a + ", B is " + b + ", and C is " + (int) c + ".");
					System.out.println("A + B + C sums to " + 1000 + ".");
					System.out.print("The product of A, B, and C is ");
					return (a * b * (int) c);
				}
			}
		}
		return 0;
	}
}
