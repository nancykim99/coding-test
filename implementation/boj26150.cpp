/*
BOJ26150 : Identify, Sort, Index, Solve (S5)

해결 방법 : 전부 입력 받고, sorting 후, 각 단어에서 인덱스 - 1의 문자를 꺼내기
*/

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cctype>

using namespace std;

struct Info {
  int num;
  string word;
  int rank;
};

int main() {
  int n;
  cin >> n;
  vector<Info> arr;
  for (int i = 0; i < n; i++) {
    string word;
    int num, rank;
    cin >> word >> num >> rank;
    arr.push_back({num, word, rank});
  }
  sort(arr.begin(), arr.end(), [](const Info& a, const Info& b) {
    return a.num < b.num;
  });
  string ans = "";
  for (int i = 0; i < n; i++) {
    int rank = arr[i].rank;
    char temp = arr[i].word[rank-1];
    temp = toupper(temp);
    ans += temp;
  }
  cout << ans << '\n';
};
