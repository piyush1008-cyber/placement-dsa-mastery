"""
Problem: Trapping Rain Water (LeetCode #42)
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it can trap after raining.

Time Complexity: O(N) - two pointer traversal
Space Complexity: O(1) - in-place constant space
"""
from typing import List


def trap_rain_water(height: List[int]) -> int:
    """Calculates volume of trapped rainwater using two pointers."""
    if not height:
        return 0

    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    water_volume = 0

    while left < right:
        if left_max < right_max:
            left += 1
            left_max = max(left_max, height[left])
            water_volume += max(0, left_max - height[left])
        else:
            right -= 1
            right_max = max(right_max, height[right])
            water_volume += max(0, right_max - height[right])

    return water_volume


if __name__ == "__main__":
    heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    res = trap_rain_water(heights)
    print(f"Trapped water for {heights}: {res}")
    assert res == 6
