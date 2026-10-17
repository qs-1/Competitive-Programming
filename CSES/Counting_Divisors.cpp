#include <iostream>

using namespace std;

int solve(int x) {
    int ans = 1;
    int i = 2;
    while (i * i <= x) { // perfect sq <=
        int prime = 1;
        while (x % i == 0) {
            x /= i;
            prime++;
        }
        if (prime > 1) ans *= prime;
        i++;
    }
    return ans * (x > 1 ? 2 : 1); // leftover prime fact
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int cases;
    if (!(cin >> cases)) return 0;
    while (cases--) {
        int n;
        cin >> n;
        cout << solve(n) << "\n";
    }

    return 0;
}
