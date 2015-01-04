
public class Euler1 {
	private static int max = 100;
	public static void main(String[] args) {
		System.out.println(findSum());
	}
	
	private static int findSum() {
		int total = 0;
		for (int i = 3; i < max; i++) {
			if (i % 3 == 0 || i % 5 == 0) total += i;
		}
		return total;
	}
}
