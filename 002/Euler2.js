(function euler2() {
	var sum = 0;
	var a = 0;
	var b = 1;
	var c;
	for (c = a + b; c < 4000000;){
		c = a + b;
		a = b;
		b = c;
		if (c % 2 === 0){
			sum += c;
		}
	}
	console.log(sum);
	return sum;
})();

