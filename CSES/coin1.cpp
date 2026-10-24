#include <bits/stdc++.h>
using namespace std;

const long long MOD = 1000000007LL;

int main() {
    int n, target;
    scanf("%d %d", &n, &target);

    vector<int> coins(n);
    for (auto &c : coins) scanf("%d", &c);
    sort(coins.begin(), coins.end());

    vector<long long> dp(target + 1, 0);
    dp[0] = 1;

    for (int curr = 1; curr <= target; curr++) {
        for (int coin : coins) {
            if (coin > curr) break;
            dp[curr] = dp[curr] + dp[curr - coin];
        }
        dp[curr] %= MOD;
    }

    printf("%lld\n", dp[target]);
    return 0;
}