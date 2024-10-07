#include <stdio.h>

int main(){
  int s[30] = {0};
  int a = 0;
  for(int i = 0;i < 28;i++){
    scanf("%d", &a);
    s[a-1] = 1;
  }
  for(int i = 0;i < 30;i++){
    if(s[i] == 0){
      printf("%d\n", i+1);
    }
  }
    
}