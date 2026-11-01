/**
 * Problem: Course Schedule - Cycle Detection & Topological Sort (LeetCode #207)
 * Time Complexity: O(V + E)
 * Space Complexity: O(V + E)
 */
#include <iostream>
#include <vector>
#include <queue>
#include <cassert>

bool canFinish(int numCourses, const std::vector<std::vector<int>>& prerequisites) {
    std::vector<std::vector<int>> adj(numCourses);
    std::vector<int> indegree(numCourses, 0);

    for (const auto& edge : prerequisites) {
        adj[edge[1]].push_back(edge[0]);
        indegree[edge[0]]++;
    }

    std::queue<int> q;
    for (int i = 0; i < numCourses; ++i) {
        if (indegree[i] == 0) q.push(i);
    }

    int completed = 0;
    while (!q.empty()) {
        int curr = q.front();
        q.pop();
        completed++;

        for (int neighbor : adj[curr]) {
            indegree[neighbor]--;
            if (indegree[neighbor] == 0) {
                q.push(neighbor);
            }
        }
    }
    return completed == numCourses;
}

int main() {
    assert(canFinish(2, {{1, 0}}) == true);
    assert(canFinish(2, {{1, 0}, {0, 1}}) == false);
    std::cout << "[PASS] Course Schedule Topological Sort C++ Implementation" << std::endl;
    return 0;
}
