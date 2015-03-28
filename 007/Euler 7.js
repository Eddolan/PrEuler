(function euler7() {
  // recursive implementation of euler7
  // goal is to find hte 10,001st prime number
  var primeListGenerator = function(n){
    // finds a list of n prime numbers recursibly
    var primes = [2];
    for (var x = 3; primes.length < n; x += 2){
      var isPrime = true;
      for (var i = 0; i < primes.length; i++){
        if (x % primes[i] === 0){
          isPrime = false;
          break;
        }
      }
      if (isPrime){
        primes.push(x);
      }
    }
    return primes;
  };

  var primeGenerator = function(n){
    // finds all prime numbers up to n recursivly
    // base case is returning first prime number
    if (n <= 2){
      return [2];
    }
    var sqrt = Math.floor(Math.sqrt(n));
    // getting a list of all primes up to sqrt n
    var rootPrimes = primeGenerator(sqrt);
    // iterating through all odd numbers from sqrt to n and checking
    // if its divisible by any of the existing primes
    var isPrime;
    for (var x = sqrt % 2 ? sqrt + 2 : sqrt + 1; x <= n; x += 2){
      isPrime = true;
      for (var i = 0; i < rootPrimes.length; i++){
        if (x % rootPrimes[i] === 0){
          isPrime = false;
          break;
        }
      }
      if (isPrime){
        rootPrimes.push(x);
      }
    }
    return rootPrimes;
  };

  var result = primeListGenerator(10001).pop();
  console.log(result);
  return result;

})();
