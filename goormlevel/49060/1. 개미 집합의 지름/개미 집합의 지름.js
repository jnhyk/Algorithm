const readline = require('readline');

const two = (n, d, l) => {
    let result = 0;
    let st = 0;
    let ed = 0;
    while (st < n && ed < n) {
        if (l[ed] - l[st] <= d) {
            result = Math.max(result, ed - st + 1);
            ed++;
        } else {
            st++;
        }
    }
    return n - result;
};

(async () => {
    const rl = readline.createInterface({ input: process.stdin });
    const input = [];
    for await (const line of rl) {
        input.push(line.split(" ").map(Number));
    }
    rl.close();

    let [n, d] = input.shift();
    let l = input[0];
    l.sort((a, b) => a - b);

    console.log(two(n, d, l));
    process.exit();
})();
