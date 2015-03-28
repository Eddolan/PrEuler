// solution comes from Nicolas Gallagher

(function euler5() {
  var num = 0;
  var i = 1;
  var maxDivisor = 20;
  var found = false;

  while (found === false) {
    num += maxDivisor;
    while (num % i === 0 && i <= maxDivisor) {
      if (i === maxDivisor) {
        found = true;
      }
      i++;
    }
    i = 1;
  }
  console.log(num);
  return num;
})();

