"""
Problem: Maximum Subarray - Kadane's Algorithm (LeetCode #53)
Given an integer array nums, find the subarray with the largest sum, and return its sum.

Time Complexity: O(N) - single pass linear scan
Space Complexity: O(1) - constant auxiliary memory
"""
from typing import List


def max_sub_array(nums: List[int]) -> int:
    """Computes maximum contiguous subarray sum using Kadane's algorithm."""
    if not nums:
        raise ValueError("Input array must be non-empty")
        
    current_sum = nums[0]
    max_sum = nums[0]
    
    for x in nums[1:]:
        current_sum = max(x, current_sum + x)
        max_sum = max(max_sum, current_sum)
        
    return max_sum


if __name__ == "__main__":
    test_arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    ans = max_sub_array(test_arr)
    print(f"Max contiguous subarray sum for {test_arr}: {ans}")
    assert ans == 6  # Subarray [4, -1, 2, 1] has the largest sum = 6
