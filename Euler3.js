
var isPrime = function(num){
	if (num == 2){ return True };
	limit = Math.floor(Math.sqrt(num));
	console.log(limit)
	for (var i = 3; i <= limit; i = i + 2){
		if (num == 486847){ console.log(i)}
		if (num % i == 0 ){ return false};
	return true;
	};
};

var isFactor = function(num, factor){
	return (num % factor == 0);
}

var largestFactor = function(num){
	limit = Math.floor(Math.sqrt(num));
	for (var i = limit;i >= 2; i -= 1){
		if (isFactor(num, i)){
			if (isPrime(i)){
				return i;
			}
		};
	}
};
console.log(largestFactor(600851475143))
