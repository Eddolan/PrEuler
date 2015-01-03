function euler2() {
	var sum = 0;
	var a = 0
	var b = 1
	for (var c = a + b; c < 4000000;){
		c = a + b;
		a = b;
		b = c;
		if (c % 2 == 0){
			console.log(c)
			sum += c
		}
	}
	return sum
}

console.log(euler2())