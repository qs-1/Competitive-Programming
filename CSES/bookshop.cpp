#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, maxprice;
    scanf("%d %d", &n, &maxprice);

    vector<int> prices(n), pages(n);
    for (auto &v : prices) scanf("%d", &v);
    for (auto &v : pages) scanf("%d", &v);

    vector<vector<int>> dp(n + 1, vector<int>(maxprice + 1, 0));

    for (int i = 1; i <= n; i++) {
        for (int budget = 0; budget <= maxprice; budget++) {
            int skip = dp[i - 1][budget];
            int take = 0;
            if (prices[i - 1] <= budget) {
                take = pages[i - 1] + dp[i - 1][budget - prices[i - 1]];
            }
            dp[i][budget] = max(skip, take);
        }
    }

    printf("%d\n", dp[n][maxprice]);
    return 0;
}