"""
Problem: Container With Most Water (LeetCode #11)
Find two lines that together with the x-axis form a container, such that the container contains the most water.

Time Complexity: O(N) - two pointer inward convergence
Space Complexity: O(1) - constant memory
"""
from typing import List


def max_area(height: List[int]) -> int:
    """Calculates max area between two vertical lines."""
    left, right = 0, len(height) - 1
    max_water = 0

    while left < right:
        width = right - left
        h = min(height[left], height[right])
        max_water = max(max_water, width * h)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water


if __name__ == "__main__":
    heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    ans = max_area(heights)
    print(f"Max water area: {ans}")
    assert ans == 49
