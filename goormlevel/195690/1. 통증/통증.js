const readline = require('readline');
let rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout,
});
let input;
rl.on('line', (line) => {
	input = line;
	rl.close();
});

rl.on('close', () => {
	let a = new Array(14,7,1)
	var cnt = 0
	while(input > 0){
		a.some(function(i){
			if (input >= i){
				input -= i
				cnt += 1
				return true
			}
			else{
				return false
			}
		})
	}
	console.log(cnt);
})