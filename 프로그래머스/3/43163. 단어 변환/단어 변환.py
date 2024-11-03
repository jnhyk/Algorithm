def findStr(str1, str2):
    diff_count = sum(1 for a, b in zip(str1, str2) if a != b)
    return diff_count == 1

def chooseStrs(str1, strings, visited):
    return [s for s in strings if findStr(str1, s) and not visited[strings.index(s)]]

def dfs(begin, target, words, visited):
    l = chooseStrs(begin, words, visited)
    a = 0
    if begin == target:
        return 0
    if not l:
        return -50
    for i in l:
        if not visited[words.index(i)]:
            visited[words.index(i)] = 1
            a = dfs(i, target, words, visited)
            visited[words.index(i)] = 0
    return a + 1
    


def solution(begin, target, words):
    if target not in words:
        return 0
    visited = [0 for _ in range(len(words))]
    answer = dfs(begin, target, words, visited)
    return answer