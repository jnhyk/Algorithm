// Run by Node.js

const readline = require("readline");
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});
let input
rl.on("line", function(line) {
	input = line.trim()
	rl.close();
}).on("close", function() {
	let a = input.split(" ").filter((e) => e !== "")
	console.log(a.length)
	process.exit();
});