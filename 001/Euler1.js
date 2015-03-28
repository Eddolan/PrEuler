(function euler1() {
  var sum = 0;
  for (var x = 0; x<1000; x++){
    if (x % 3 === 0 || x % 5 === 0) {
      sum += x;
    }
  }
  console.log(sum);
  return sum;
})();
