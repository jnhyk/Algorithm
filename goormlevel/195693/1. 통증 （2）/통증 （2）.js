const readline = require('readline');
let rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout,
});
let input = [];
rl.on('line', (line) => {
	input.push(line.split(" ").map(Number));
});

rl.on('close', () => {
	let [n] = input.shift()
	let [a,b] = input[0]
	let cnt = 0
	let o_n = n
	cnt += Math.floor(n / b) //0
	n %= b // 11
	while(n){
		if (n == o_n && n%a != 0){
			cnt = -1
			break
		}
		if (n%a != 0){
			n += b
			cnt -= 1
		}
		else{
			cnt += n/a
			n = 0
			break
		}
	}
	console.log(cnt)
})