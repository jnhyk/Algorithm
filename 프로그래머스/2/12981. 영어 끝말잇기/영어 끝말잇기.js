function solution(n, words) {
    var answer = [0,0];
    let l
    for(var i = 0 ;i < words.length;i++){
        if (i == 0){
            l = words[i].slice(-1)
            continue
        }
        if (l !== words[i][0] || words.slice(0,i).includes(words[i])||words[i].length == 1){
            answer[0] = i % n + 1
            if ((i+1) % n == 0){
                answer[1] = Math.floor((i+1) / n)
            }
            else{
                answer[1] = Math.floor((i+1) / n) + 1
            }
            break
        }
        else{
            l = words[i].slice(-1)
        }
        
    }

    return answer;
}