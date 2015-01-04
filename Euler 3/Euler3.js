
var isPrime = function(num){
	if (num == 2){
		return true;
	}
	var limit1 = Math.floor(Math.sqrt(num));
	if (num % 2 == 0){
		return false;
	}
	for (var x = 3; x < limit1; x = x + 2){
		if (num % x == 0 ){ return false}
	}
	return true;
};

var isFactor = function(num, factor){
	return (num % factor == 0);
};

var getFactors = function(num){
	var result = [];
	limit = Math.floor(Math.sqrt(num));
	for (var i = limit;i >= 2; i -= 1) {
		if (isFactor(num, i) && isPrime(i)) {
			result.push(i);
		}
	}
	console.log(result)
	return result;
};


var largestFactor = function(num){
	return getFactors(num).shift();
};

console.log(largestFactor(600851475143))
