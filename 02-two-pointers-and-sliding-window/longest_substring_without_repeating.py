"""
Problem: Longest Substring Without Repeating Characters (LeetCode #3)
Given a string s, find the length of the longest substring without repeating characters.

Time Complexity: O(N) - sliding window with index map
Space Complexity: O(min(N, M)) - character map
"""


def length_of_longest_substring(s: str) -> int:
    """Finds length of longest contiguous substring with distinct characters."""
    char_index_map = {}
    max_length = 0
    start = 0

    for end, char in enumerate(s):
        if char in char_index_map and char_index_map[char] >= start:
            start = char_index_map[char] + 1
        char_index_map[char] = end
        max_length = max(max_length, end - start + 1)

    return max_length


if __name__ == "__main__":
    test_str = "abcabcbb"
    ans = length_of_longest_substring(test_str)
    print(f"Longest non-repeating substring length for '{test_str}': {ans}")
    assert ans == 3  # "abc"
