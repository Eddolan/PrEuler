(function euler3() {

	var isPrime = function(num){
		if (num == 2){
			return true;
		}
		var limit = Math.floor(Math.sqrt(num));
		if (num % 2 === 0){
			return false;
		}
		for (var x = 3; x < limit; x = x + 2){
			if (num % x === 0 ){
				return false;
			}
		}
		return true;
	};

	var isFactor = function(num, factor){
		return (num % factor === 0);
	};

	var getFactors = function(num){
		var result = [];
		var limit = Math.floor(Math.sqrt(num));
		for (var i = limit;i >= 2; i -= 1) {
			if (isFactor(num, i) && isPrime(i)) {
				result.push(i);
			}
		}
		return result;
	};

	var result = getFactors(600851475143).shift();
	console.log(result);
	return result;
})();
