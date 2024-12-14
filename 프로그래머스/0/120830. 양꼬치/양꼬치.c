#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
//음료수 먹은거 빼줄게~
int solution(int n, int k) {
    int answer = 0;
    int service = n / 10;
    answer = n * 12000 + (k-service) * 2000;
    return answer;
}
    