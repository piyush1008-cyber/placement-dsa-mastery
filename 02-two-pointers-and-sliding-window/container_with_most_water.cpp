/**
 * Problem: Container With Most Water (LeetCode #11)
 * Time Complexity: O(N)
 * Space Complexity: O(1)
 */
#include <iostream>
#include <vector>
#include <algorithm>
#include <cassert>

int maxArea(const std::vector<int>& height) {
    int left = 0, right = static_cast<int>(height.size()) - 1;
    int maxWater = 0;

    while (left < right) {
        int width = right - left;
        int h = std::min(height[left], height[right]);
        maxWater = std::max(maxWater, width * h);

        if (height[left] < height[right]) {
            left++;
        } else {
            right--;
        }
    }
    return maxWater;
}

int main() {
    std::vector<int> heights = {1, 8, 6, 2, 5, 4, 8, 3, 7};
    int ans = maxArea(heights);
    assert(ans == 49);
    std::cout << "[PASS] Container With Most Water C++ Implementation" << std::endl;
    return 0;
}
