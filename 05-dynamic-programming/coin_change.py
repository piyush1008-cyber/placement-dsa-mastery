"""
Problem: Coin Change (LeetCode #322)
You are given an integer array coins representing coins of different denominations and an integer amount.
Return the fewest number of coins that you need to make up that amount.

Time Complexity: O(amount * len(coins)) - bottom-up tabular DP
Space Complexity: O(amount)
"""
from typing import List


def coin_change(coins: List[int], amount: int) -> int:
    """Computes minimum coins needed to make change for amount."""
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0

    for a in range(1, amount + 1):
        for c in coins:
            if a - c >= 0:
                dp[a] = min(dp[a], 1 + dp[a - c])

    return dp[amount] if dp[amount] != float("inf") else -1


if __name__ == "__main__":
    assert coin_change([1, 2, 5], 11) == 3   # 5 + 5 + 1 = 11 (3 coins)
    assert coin_change([2], 3) == -1
    assert coin_change([1], 0) == 0
    print("[PASS] Coin Change DP Python Implementation")
