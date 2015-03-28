(function euler6() {

  var each = function(n, cb){
    // iterates through all numbers 1..n and performs callback
    for (var i = 1; i <= n; i++){
      cb(i);
    }
  };

  var sumSquares = function(n){
    var sum = 0;
    each(n, function(i){
      sum += i;
    });
    return sum * sum;
  };

  var sqauresSum = function(n){
    var sum = 0;
    each(n, function(i){
      sum += i * i;
    });
    return sum;
  };

  var result = sumSquares(100) - sqauresSum(100);
  return result;

})();
