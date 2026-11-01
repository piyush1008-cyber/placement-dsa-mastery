/**
 * Problem: Two Sum (LeetCode #1)
 * Time Complexity: O(N) - single pass hash table
 * Space Complexity: O(N) - unordered_map complement storage
 */
#include <iostream>
#include <vector>
#include <unordered_map>
#include <cassert>

std::vector<int> twoSum(const std::vector<int>& nums, int target) {
    std::unordered_map<int, int> seen; // value -> index
    for (int i = 0; i < static_cast<int>(nums.size()); ++i) {
        int complement = target - nums[i];
        if (seen.find(complement) != seen.end()) {
            return {seen[complement], i};
        }
        seen[nums[i]] = i;
    }
    return {};
}

int main() {
    std::vector<int> nums = {2, 7, 11, 15};
    int target = 9;
    std::vector<int> result = twoSum(nums, target);
    assert(result.size() == 2 && result[0] == 0 && result[1] == 1);
    std::cout << "[PASS] Two Sum C++ Implementation" << std::endl;
    return 0;
}
