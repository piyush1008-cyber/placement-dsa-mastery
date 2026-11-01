# 🧠 Placement DSA Mastery (C++ & Python)

[![CI Test Suite](https://github.com/piyush1008-cyber/placement-dsa-mastery/actions/workflows/ci.yml/badge.svg)](https://github.com/piyush1008-cyber/placement-dsa-mastery/actions/workflows/ci.yml)
![C++](https://img.shields.io/badge/C++-17-00599C?style=for-the-badge&logo=c%2B%2B&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)
![LeetCode](https://img.shields.io/badge/LeetCode-Curated%20Top%20Interview-FFA116?style=for-the-badge&logo=leetcode&logoColor=black)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

> **Curated, production-grade solutions for Top Technical Interview & Campus Placement Coding Questions in both modern C++17 and Python 3, annotated with detailed time/space complexity analysis.**

---

## 📌 Topic Index & Progress

| Topic | Key Algorithms / Patterns Covered | C++ | Python | Difficulty |
|---|---|:---:|:---:|:---:|
| **Arrays & Hashing** | Kadane's Algorithm, Two Sum, 3Sum, Trapping Rain Water, Longest Consecutive Sequence | ✅ | ✅ | Medium / Hard |
| **Two Pointers & Sliding Window** | Container With Most Water, Longest Substring Without Repeating Characters, Min Window Substring | ✅ | ✅ | Medium / Hard |
| **Linked Lists** | In-place Reversal, Cycle Detection (Floyd's Tortoise & Hare), LRU Cache, Merge K Sorted Lists | ✅ | ✅ | Medium / Hard |
| **Trees & Graphs** | Level Order Traversal, LCA, Number of Islands (BFS/DFS), Course Schedule (Topological Sort) | ✅ | ✅ | Medium |
| **Dynamic Programming** | 0/1 Knapsack, Coin Change, Longest Increasing Subsequence (LIS), House Robber | ✅ | ✅ | Medium / Hard |

---

## 📁 Repository Organization

```
placement-dsa-mastery/
├── 01-arrays-and-hashing/
│   ├── two_sum.cpp & two_sum.py
│   ├── kadanes_max_subarray.cpp & kadanes_max_subarray.py
│   ├── three_sum.cpp & three_sum.py
│   └── trapping_rain_water.cpp & trapping_rain_water.py
├── 02-two-pointers-and-sliding-window/
│   ├── container_with_most_water.cpp & container_with_most_water.py
│   └── longest_substring_without_repeating.cpp & longest_substring_without_repeating.py
├── 03-linked-lists/
│   ├── reverse_linked_list.cpp & reverse_linked_list.py
│   └── lru_cache.cpp & lru_cache.py
├── 04-trees-and-graphs/
│   ├── lowest_common_ancestor.cpp & lowest_common_ancestor.py
│   ├── number_of_islands.cpp & number_of_islands.py
│   └── course_schedule_topo.cpp & course_schedule_topo.py
├── 05-dynamic-programming/
│   ├── coin_change.cpp & coin_change.py
│   ├── longest_increasing_subsequence.cpp & longest_increasing_subsequence.py
│   └── zero_one_knapsack.cpp & zero_one_knapsack.py
├── tests/
│   └── run_all_tests.py
├── .gitignore
├── LICENSE
└── README.md
```

---

## ⚡ Complexity Quick Reference

| Problem | Time Complexity | Space Complexity | Paradigm |
|---|:---:|:---:|---|
| **Two Sum** | $O(N)$ | $O(N)$ | Hash Map Lookups |
| **Kadane's Subarray** | $O(N)$ | $O(1)$ | Dynamic Programming / Greedy |
| **Trapping Rain Water** | $O(N)$ | $O(1)$ | Two Pointers |
| **LRU Cache** | $O(1)$ amortized | $O(C)$ | Doubly-Linked List + Hash Map |
| **Number of Islands** | $O(M \times N)$ | $O(M \times N)$ | BFS / DFS Flood Fill |
| **Course Schedule** | $O(V + E)$ | $O(V + E)$ | Kahn's Algorithm (Kahn's / Indegree) |
| **Coin Change** | $O(N \times \text{amount})$ | $O(\text{amount})$ | Bottom-Up DP |
| **Longest Increasing Subseq (LIS)** | $O(N \log N)$ | $O(N)$ | Patience Sorting + Binary Search |

---

## 🧪 Running Automated Tests

Run the built-in Python test suite validating all implementations across sample and edge cases:

```bash
python tests/run_all_tests.py
```

---

## 👤 Author

**Peeyoosh Kangle**
- 📧 Email: piyushkangle@gmail.com
- 🐙 GitHub: [github.com/piyush1008-cyber](https://github.com/piyush1008-cyber)

---

## 📄 License

This repository is distributed under the MIT License — see the [LICENSE](LICENSE) file.
