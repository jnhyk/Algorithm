const readline = require('readline');
let rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout,
});
let input = [];
const dx = [0, 1, 0, -1];
const dy = [1, 0, -1, 0];
rl.on('line', (line) => {
	input.push(line.split(" ").map(Number));
});

rl.on('close', () => {
	let [n] = input.shift()
	let visited = Array(n).fill(0).map((i) => Array(n).fill(false))
	let result = 0;
  for (let i = 0; i < n; ++i) {
		for (let j = 0; j < n; ++j) {
			if (input[i][j] !== 1 || visited[i][j]) continue;
			++result;
			const tmp = [[i, j]];

			while (tmp.length) {
				let [currI, currJ] = tmp.pop();
				visited[currI][currJ] = true;

				for (let k = 0; k < 4; ++k) {
					const ni = currI + dx[k];
					const nj = currJ + dy[k];
					if (ni < 0 || ni >= n || nj < 0 || nj >= n) continue;
					if (input[ni][nj] !== 1 || visited[ni][nj]) continue;
					tmp.push([ni, nj]);
				}
			}
		}
	}
	console.log(result);
})