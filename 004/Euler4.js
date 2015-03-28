(function euler4() {

  var isPalendrome = function(num){
    var numArray = num.toString().split('');
    while (numArray.length > 1){
      if (numArray.pop() != numArray.shift()){
        return false;
      }
    }
    return true;
  };

  var testNum;
  var max = 0;
  for (var x = 999; x >= 100; x--) {
    for (var y = 999; y >= 100; y--) {
      testNum = x * y;
      if (isPalendrome(testNum) && testNum > max) {
        max = testNum;
      }
    }
  }
  console.log(max);
  return max;
})();