// Project euler 1

e1 = function() {
	var sum = 0;
	for(var i = 1; i < 1000; i++) {
		if(i % 3 == 0 || i % 5 == 0) {
			sum += i;
		}
	}
	return sum
}

console.log(e1());
