/**
 * Problem: Trapping Rain Water (LeetCode #42)
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */
#include <iostream>
#include <vector>
#include <algorithm>
#include <cassert>

int trap(const std::vector<int>& height) {
    if (height.empty()) return 0;

    int left = 0, right = static_cast<int>(height.size()) - 1;
    int leftMax = height[left], rightMax = height[right];
    int trappedWater = 0;

    while (left < right) {
        if (leftMax < rightMax) {
            left++;
            leftMax = std::max(leftMax, height[left]);
            trappedWater += std::max(0, leftMax - height[left]);
        } else {
            right--;
            rightMax = std::max(rightMax, height[right]);
            trappedWater += std::max(0, rightMax - height[right]);
        }
    }
    return trappedWater;
}

int main() {
    std::vector<int> heights = {0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1};
    int totalWater = trap(heights);
    assert(totalWater == 6);
    std::cout << "[PASS] Trapping Rain Water C++ Implementation" << std::endl;
    return 0;
}
