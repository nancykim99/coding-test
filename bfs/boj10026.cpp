/*
BOJ10026 : 적록색약 (G5)

해결 방법 : 
*/

#include <iostream>
#include <vector>
#include <deque>

using namespace std;

int main() {
    int n;
    cin >> n;
    vector<vector<string>> area;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            string m;
            cin >> m;
            area[i][j] = m;
        }
    }
}

int bfs() {

}