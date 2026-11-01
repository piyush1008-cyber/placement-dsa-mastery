"""
Problem: Number of Islands (LeetCode #200)
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water),
return the number of islands.

Time Complexity: O(M * N)
Space Complexity: O(M * N) - recursion call stack or BFS queue
"""
from typing import List
from collections import deque


def num_islands(grid: List[List[str]]) -> int:
    """Counts connected components of land using Breadth-First Search (BFS)."""
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = set()
    islands = 0

    def bfs(r: int, c: int) -> None:
        queue = deque([(r, c)])
        visited.add((r, c))
        while queue:
            curr_r, curr_c = queue.popleft()
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = curr_r + dr, curr_c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1" and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in visited:
                bfs(r, c)
                islands += 1

    return islands


if __name__ == "__main__":
    test_grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    res = num_islands(test_grid)
    print(f"Number of islands: {res}")
    assert res == 3
