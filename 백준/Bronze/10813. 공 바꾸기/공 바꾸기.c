#include <stdio.h>

int main(){
  int n = 0;
  int m = 0;
  int a,b;
  int temp;
  int basket[100] = {0};
  scanf("%d %d", &n, &m);
  for(int i = 0; i < n;i++){
    basket[i] = i+1;
  }
  for (int i = 0; i < m; i++){
    scanf("%d %d", &a, &b);
    temp = basket[a-1];
    basket[a-1] = basket[b-1];
    basket[b-1] = temp;
  }
  for(int i = 0; i < n;i++){
    printf("%d ", basket[i]);
  }
}