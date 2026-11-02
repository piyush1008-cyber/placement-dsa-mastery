"""
LeetCode 15: 3Sum
Difficulty: Medium
Pattern: Two Pointers + Sorting
Time Complexity: O(n^2)
Space Complexity: O(1) auxiliary (excluding output array)

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.
"""
from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    triplets = []
    n = len(nums)

    for i in range(n - 2):
        # Skip identical elements to avoid duplicate triplets
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = n - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            if current_sum == 0:
                triplets.append([nums[i], nums[left], nums[right]])

                # Skip duplicate left values
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                # Skip duplicate right values
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1
            elif current_sum < 0:
                left += 1
            else:
                right -= 1

    return triplets
