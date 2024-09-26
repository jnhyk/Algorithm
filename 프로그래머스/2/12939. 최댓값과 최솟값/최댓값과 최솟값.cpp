#include <string>
#include <vector>
#include <sstream>
#include <algorithm>
#include <iostream>

using namespace std;

string solution(string s) {
    string answer = "";
    vector<int> vect;
    stringstream ss(s);
    int number;
    
    while (ss >> number) {
        vect.push_back(number);
    }
    int a = *max_element(vect.begin(), vect.end());
    int b = *min_element(vect.begin(), vect.end());
    answer = to_string(b) + " " + to_string(a);
    return answer;
}