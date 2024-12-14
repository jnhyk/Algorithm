#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
//전체 금액에서 서비스 받은만큼 돈으로 빼요
int solution(int n, int k) {
    return n * 12000 + k * 2000 - (n / 10 * 2000);
}
    