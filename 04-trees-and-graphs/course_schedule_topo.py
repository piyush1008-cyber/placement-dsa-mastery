"""
Problem: Course Schedule - Cycle Detection & Topological Sort (LeetCode #207)
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
Determine if you can finish all courses.

Time Complexity: O(V + E) - Kahn's Algorithm
Space Complexity: O(V + E) - Adjacency list and indegree array
"""
from typing import List
from collections import deque


def can_finish(num_courses: int, prerequisites: List[List[int]]) -> bool:
    """Verifies whether DAG possesses a valid topological ordering (no cycles)."""
    adj = {i: [] for i in range(num_courses)}
    indegree = [0] * num_courses

    for course, prereq in prerequisites:
        adj[prereq].append(course)
        indegree[course] += 1

    queue = deque([i for i in range(num_courses) if indegree[i] == 0])
    completed_courses = 0

    while queue:
        curr = queue.popleft()
        completed_courses += 1
        for neighbor in adj[curr]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return completed_courses == num_courses


if __name__ == "__main__":
    assert can_finish(2, [[1, 0]]) is True
    assert can_finish(2, [[1, 0], [0, 1]]) is False  # Circular dependency
    print("[PASS] Course Schedule Topological Sort Python Implementation")
