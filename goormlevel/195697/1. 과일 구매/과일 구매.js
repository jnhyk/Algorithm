const readline = require('readline');
let rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout,
});
let input = [];
rl.on('line', (line) => {
	input.push(line.split(" ").map(Number)); // 입력 값을 숫자로 변환하여 저장
});

rl.on('close', () => {
	let [n, k] = input.shift(); // 첫 번째 줄에서 n과 k 값을 분리
	let c = 0;
	let pieces = input.map((item) => item[1] / item[0]); // 각 항목의 가치 비율 계산

	while (k > 0) {
		if (input.length === 0) {
			break;
		}
		let max = Math.max(...pieces);
		let maxIndex = pieces.indexOf(max);

		if (input[maxIndex][0] <= k) {
			c += input[maxIndex][1];
			k -= input[maxIndex][0];
			input.splice(maxIndex, 1); // 사용한 항목 제거
			pieces.splice(maxIndex, 1); // 사용한 항목의 비율 제거
		} else {
			c += k * pieces[maxIndex];
			k = 0;
		}
	}
	console.log(c);
});
