#include <bits/stdc++.h>
using namespace std;

int min_protections(int n, int k, const string &s) {
    int ans = 0;
    int j = 0;
    bool flag = true;

    for (int i = 0; i < n; i++) {
        if (s[i] == '1' && flag == false) {
            if (i - j > k - 1) {
                ans++;
                j = i;
            } else {
                j = i;
            }
        } else if (s[i] == '1' && flag == true) {
            ans++;
            flag = false;
            j = i;
        }
    }

    return ans;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while (t--) {
        int n, k;
        cin >> n >> k;
        string s;
        cin >> s;  // string input (e.g., "10101")
        cout << min_protections(n, k, s) << "\n";
    }

    return 0;
}
