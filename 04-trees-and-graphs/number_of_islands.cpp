/**
 * Problem: Number of Islands (LeetCode #200)
 * Time Complexity: O(M * N)
 * Space Complexity: O(M * N)
 */
#include <iostream>
#include <vector>
#include <cassert>

void dfs(std::vector<std::vector<char>>& grid, int r, int c) {
    int rows = static_cast<int>(grid.size());
    int cols = static_cast<int>(grid[0].size());
    if (r < 0 || c < 0 || r >= rows || c >= cols || grid[r][c] != '1') return;

    grid[r][c] = '0'; // mark visited in-place
    dfs(grid, r - 1, c);
    dfs(grid, r + 1, c);
    dfs(grid, r, c - 1);
    dfs(grid, r, c + 1);
}

int numIslands(std::vector<std::vector<char>>& grid) {
    if (grid.empty() || grid[0].empty()) return 0;
    int islands = 0;
    for (int r = 0; r < static_cast<int>(grid.size()); ++r) {
        for (int c = 0; c < static_cast<int>(grid[0].size()); ++c) {
            if (grid[r][c] == '1') {
                islands++;
                dfs(grid, r, c);
            }
        }
    }
    return islands;
}

int main() {
    std::vector<std::vector<char>> grid = {
        {'1', '1', '0', '0', '0'},
        {'1', '1', '0', '0', '0'},
        {'0', '0', '1', '0', '0'},
        {'0', '0', '0', '1', '1'}
    };
    int ans = numIslands(grid);
    assert(ans == 3);
    std::cout << "[PASS] Number of Islands C++ Implementation" << std::endl;
    return 0;
}
