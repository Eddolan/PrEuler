
public class Euler4 {
	public static void main(String[] args) {
		System.out.println(largestPalindrome());
	}
	
	private static int largestPalindrome() {
		int max = 0;
		for (int i = 999; i >= 100; i--) {
			for (int j = 999; j >= 100; j--) {
				int num = i * j;
				if (parse(num)) {
					if (num > max) {
						max = num;
					}
				}
			}
		}
		return max;
	}
	
	private static Boolean parse(Integer num) {
		String str = Integer.toString(num);
		for (int k = 0; k < str.length()/2; k++) {
			if (str.charAt(k) != str.charAt(str.length() - 1 - k)) return false;
		}
		return true;
	}
}
