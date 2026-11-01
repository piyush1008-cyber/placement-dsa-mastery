/**
 * Problem: Maximum Subarray - Kadane's Algorithm (LeetCode #53)
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */
#include <iostream>
#include <vector>
#include <algorithm>
#include <cassert>

int maxSubArray(const std::vector<int>& nums) {
    if (nums.empty()) return 0;
    int currentSum = nums[0];
    int maxSum = nums[0];

    for (size_t i = 1; i < nums.size(); ++i) {
        currentSum = std::max(nums[i], currentSum + nums[i]);
        maxSum = std::max(maxSum, currentSum);
    }
    return maxSum;
}

int main() {
    std::vector<int> nums = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
    int ans = maxSubArray(nums);
    assert(ans == 6);
    std::cout << "[PASS] Kadane's Algorithm C++ Implementation" << std::endl;
    return 0;
}
