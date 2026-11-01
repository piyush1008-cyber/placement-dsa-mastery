"""
Problem: Two Sum (LeetCode #1)
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

Time Complexity: O(N) - single pass hash map lookup
Space Complexity: O(N) - hash table to store complements
"""
from typing import List, Tuple, Optional


def two_sum(nums: List[int], target: int) -> Optional[Tuple[int, int]]:
    """Find indices of two numbers that sum up to target."""
    seen = {}  # val -> index
    for idx, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return (seen[complement], idx)
        seen[num] = idx
    return None


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    result = two_sum(nums, target)
    print(f"Two Sum result for {nums} with target {target}: {result}")
    assert result == (0, 1)
