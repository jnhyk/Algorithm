// Run by Node.js
const readline = require('readline');

(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	let n;
	for await (const line of rl) {
		n = Number(line)
		rl.close();
	}
	for(var i = 0 ; i < n;i++){
		console.log("*".repeat(i+1))
	}
	
	process.exit();
})();
