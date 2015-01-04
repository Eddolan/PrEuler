/**
 * Created by eddolan on 1/3/15.
 */
var isPalendrom = function(num){
    var numArray = num.toString().split('');
    while (numArray.length > 1){
        if (numArray.pop() != numArray.shift()){
            return false
        }
    }
    return true;
};

var euler4Iter = function() {
    var max = 0;
    for (var x = 999; x >= 100; x--) {
        for (var y = 999; y >= 100; y--) {
            testNum = x * y;
            if (isPalendrom(testNum) && testNum > max) {
                max = testNum;
            }
        }
    }
    return max;
};
console.log(euler4Iter());