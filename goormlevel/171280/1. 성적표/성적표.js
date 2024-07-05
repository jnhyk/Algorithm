// Run by Node.js
const readline = require('readline');

(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	let input = [];
	for await (const line of rl) {
		input.push(line.split(" ").map(Number))
	}
	let [n,m] = input.shift()
	let arr = Array(m+1)
	for(var i = 0 ;i<m+1;i++){
		arr[i] = [0,0]
	}
	input.forEach((e)=>{
		arr[e[0]][0] ++
		arr[e[0]][1] += e[1]
	})
	let avg_arr = arr.map((e)=> e[1]/e[0])
	let max = 0
	let max_index
	avg_arr.forEach((e)=>{
		if(!isNaN(e)){
			if(e > max){
				max = e
				max_index = avg_arr.indexOf(max)
			}
		}
	})
	console.log(max_index)
	
	process.exit();
})();
