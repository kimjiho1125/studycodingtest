#include <iostream>
#include <vector>

using namespace std;


void process(int n, int numOpen, int numClose, string str, vector<string>& results) {
  //종료조건 체크
  if(numOpen == n && numClose == n) {
    results.push_back(str);
    return;
  }

  //재귀
  if (numOpen < n) {
    process(n, numOpen+1, numClose, str + '(',results); // open bracket 추가
  }
  if (numClose < numOpen) {
    process(n, numOpen, numClose + 1, str + ')', results); // close bracket 추가
  }
    }

int main() {
  int n = 3;
  vector<string> results;
  process(n, 0, 0, "", results);
  
  for(const string& str: results) {
    cout << str << endl;
  }

  return 0;
}