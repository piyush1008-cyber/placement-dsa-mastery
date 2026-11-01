/**
 * Problem: Coin Change (LeetCode #322)
 * Time Complexity: O(amount * len(coins))
 * Space Complexity: O(amount)
 */
#include <iostream>
#include <vector>
#include <algorithm>
#include <cassert>

int coinChange(const std::vector<int>& coins, int amount) {
    std::vector<int> dp(amount + 1, amount + 1);
    dp[0] = 0;

    for (int a = 1; a <= amount; ++a) {
        for (int c : coins) {
            if (a - c >= 0) {
                dp[a] = std::min(dp[a], 1 + dp[a - c]);
            }
        }
    }
    return dp[amount] > amount ? -1 : dp[amount];
}

int main() {
    assert(coinChange({1, 2, 5}, 11) == 3);
    assert(coinChange({2}, 3) == -1);
    assert(coinChange({1}, 0) == 0);
    std::cout << "[PASS] Coin Change DP C++ Implementation" << std::endl;
    return 0;
}
