/*
BOJ10773 : 제로 (S4)

해결 방법 : 
문제대로 구현함.
*/

#include <iostream>
#include <vector>

using namespace std;

int main() {
  int n;
  cin >> n;
  vector<int> v;
  for (int i = 0; i < n; i++) {
    int temp;
    cin >> temp;
    if (temp != 0) {
      v.push_back(temp);
    } else {
      v.pop_back();
    }
  }
  int sum = 0;
  for (int x : v) {
    sum += x;
  }
  cout << sum << '\n';
  return 0;
}