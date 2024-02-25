#include <iostream>
#define MAX 9
using namespace std;
int arr[MAX] = {0,};
int n,m;
void f(int depth){
    if(depth ==m){
        for(int i = 0; i < m; i++){
            cout << arr[i] << " ";
        }
        cout << '\n';
        return;
    }
    for(int i = 1;i <= n;i++){//
            arr[depth] = i;
            f(depth+1);
    }
}
int main() {
    cin >> n >> m;
    f(0);
}