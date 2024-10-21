#include <stdio.h>
int main(){
  int count = 0;
  int result = 0;
  int a[11] = {0};
  int n = 0;

  for (int i = 0;i<10;i++){
    scanf("%d", &n);
    a[i] = n % 42;
  }

  for(int i = 0;i<10;i++){
    count = 0;
    for(int j = i+1;j < 10;j++){
      if(a[i] == a[j]){
        count ++;
      }
    }
    if(count == 0){
      result ++ ;
    }
  }
  printf("%d",result);
}
