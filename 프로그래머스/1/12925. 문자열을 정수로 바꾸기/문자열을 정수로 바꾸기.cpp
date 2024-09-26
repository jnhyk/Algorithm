#include <iostream>
#include <string>
#include <vector>

using namespace std;

int solution(string s) {
    int answer = 0;
    int check = 0;
    if(s[0] == '-'){
        s = s.substr(1);
        check = 1;
    }
    answer = check == 0 ? stoi(s):-stoi(s);
    return answer;
}