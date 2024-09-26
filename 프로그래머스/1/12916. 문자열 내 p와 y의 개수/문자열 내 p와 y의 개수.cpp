#include <string>
#include <iostream>
using namespace std;

bool solution(string s)
{
    bool answer = true;
    int cnt_p = 0;
    int cnt_y = 0;
    for(char c:s){
        if (c == 'p' || c == 'P'){
            cnt_p ++;
        }
        if (c == 'y' || c == 'Y'){
            cnt_y ++;
        }
    }

    answer = cnt_p == cnt_y ? true:false;

    return answer;
}