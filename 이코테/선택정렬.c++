#include<bits/stdc++.h>

using namespace std;

int n = 10;
int target[10] = {7, 5, 9, 0, 3, 1, 6, 2, 4, 8};

int main(void){

  for (int i = 0; i < n; i++){
    int min_idx = i;
    for (int j = i + 1; j < n; j++){
      if(target[min_idx] < target[j]){
        min_idx = j;
      }
    }
    int temp = target[min_idx];
    target[min_idx] = target[i];
    target[i] = temp;
  }

  for (int i = 0; i < n; i++) {
    cout << target[i] << ' ';
  }

    return 0;
}
