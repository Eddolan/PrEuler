
function euler1(){
	var sum = 0;
	for (var x = 0; x<1000; x++){
		console.log(x);
		if (x % 3 == 0 || x % 5 == 0) {
			console.log(x);
			sum += x;
		} 
	}
	return sum
	
}


console.log(euler1());