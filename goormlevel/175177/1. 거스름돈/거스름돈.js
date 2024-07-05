// Run by Node.js
const readline = require('readline');

(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	let input
	for await (const line of rl) {
		input = line
		rl.close();
	}
	let a = new Array(40,20,10,5,1)
	var cnt = 0
	while(input > 0)
	a.some(function(i){
		if (input >= i){
			input -= i
			cnt ++
			return true
		}
	})
	console.log(cnt)
	process.exit();
})();
