#include <stdio.h>

int main(){
  int n = 0;
  int max = -1000000;
  int min = 1000000;
  scanf("%d", &n);
  int a[1000000] = {0};
  for(int i = 0;i < n;i++){
    scanf("%d", &a[i]);
  }
  for(int i = 0;i < n;i++){
    if(a[i] > max){
      max = a[i];
    }
    if(a[i] < min){
      min = a[i];
    }
  }
  printf("%d %d", min, max);
  
}