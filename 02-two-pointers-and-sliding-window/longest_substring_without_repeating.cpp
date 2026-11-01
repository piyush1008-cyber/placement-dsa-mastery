/**
 * Problem: Longest Substring Without Repeating Characters (LeetCode #3)
 * Time Complexity: O(N)
 * Space Complexity: O(min(N, M)) where M is character alphabet size
 */
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cassert>

int lengthOfLongestSubstring(const std::string& s) {
    std::vector<int> lastIndex(256, -1);
    int maxLength = 0;
    int start = 0;

    for (int end = 0; end < static_cast<int>(s.length()); ++end) {
        unsigned char c = static_cast<unsigned char>(s[end]);
        if (lastIndex[c] >= start) {
            start = lastIndex[c] + 1;
        }
        lastIndex[c] = end;
        maxLength = std::max(maxLength, end - start + 1);
    }
    return maxLength;
}

int main() {
    std::string test = "abcabcbb";
    int ans = lengthOfLongestSubstring(test);
    assert(ans == 3);
    std::cout << "[PASS] Longest Substring Without Repeating Characters C++ Implementation" << std::endl;
    return 0;
}
