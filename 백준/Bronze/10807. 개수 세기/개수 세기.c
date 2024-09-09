#include <stdio.h>

int main(){
  int a[100] = {0};
  int n = 0;
  int f_num = 0;
  int count = 0;
  scanf("%d", &n);
  for(int i = 0;i < n;i++){
    scanf("%d", &a[i]);
  }
  scanf("%d", &f_num);
  for(int i = 0;i < n;i++){
    if(f_num == a[i]){
      count++;
    }
  }
  printf("%d", count);
}