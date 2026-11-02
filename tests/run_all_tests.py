"""Master test runner executing all algorithmic solution test cases."""
import sys
import os

# Ensure problem directories are discoverable
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(base_dir, "01-arrays-and-hashing"))
sys.path.insert(0, os.path.join(base_dir, "02-two-pointers-and-sliding-window"))
sys.path.insert(0, os.path.join(base_dir, "03-linked-lists"))
sys.path.insert(0, os.path.join(base_dir, "04-trees-and-graphs"))
sys.path.insert(0, os.path.join(base_dir, "05-dynamic-programming"))

from two_sum import two_sum
from three_sum import three_sum
from kadanes_max_subarray import max_sub_array
from trapping_rain_water import trap_rain_water
from container_with_most_water import max_area
from longest_substring_without_repeating import length_of_longest_substring
from lru_cache import LRUCache
from reverse_linked_list import reverse_list, to_list, from_list
from number_of_islands import num_islands
from course_schedule_topo import can_finish
from coin_change import coin_change


def run_tests():
    print("=" * 60)
    print("      RUNNING PLACEMENT DSA MASTERY ALGORITHM SUITE")
    print("=" * 60)

    # 1. Two Sum & 3Sum
    assert two_sum([2, 7, 11, 15], 9) == (0, 1)
    print(" [PASS] 01 - Two Sum")
    assert three_sum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    print(" [PASS] 01b - 3Sum (Triplets)")

    # 2. Kadane's
    assert max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    print(" [PASS] 02 - Kadane's Algorithm")

    # 3. Trapping Rain Water
    assert trap_rain_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    print(" [PASS] 03 - Trapping Rain Water")

    # 4. Container with Most Water
    assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    print(" [PASS] 04 - Container with Most Water")

    # 5. Longest Substring
    assert length_of_longest_substring("abcabcbb") == 3
    print(" [PASS] 05 - Longest Substring Without Repeating")

    # 6. LRU Cache & Reverse Linked List
    cache = LRUCache(2)
    cache.put(1, 10)
    cache.put(2, 20)
    assert cache.get(1) == 10
    cache.put(3, 30)
    assert cache.get(2) == -1
    print(" [PASS] 06 - LRU Cache Design")

    ll_head = from_list([1, 2, 3, 4, 5])
    reversed_ll = reverse_list(ll_head)
    assert to_list(reversed_ll) == [5, 4, 3, 2, 1]
    print(" [PASS] 06b - Reverse Linked List")

    # 7. Number of Islands
    grid = [
        ["1", "1", "0"],
        ["0", "1", "0"],
        ["0", "0", "1"]
    ]
    assert num_islands(grid) == 2
    print(" [PASS] 07 - Number of Islands (BFS/DFS)")

    # 8. Course Schedule
    assert can_finish(2, [[1, 0]]) is True
    assert can_finish(2, [[1, 0], [0, 1]]) is False
    print(" [PASS] 08 - Course Schedule (Topological Sort)")

    # 9. Coin Change
    assert coin_change([1, 2, 5], 11) == 3
    print(" [PASS] 09 - Coin Change (Bottom-up DP)")

    print("=" * 60)
    print(" ALL 9 CORE ALGORITHMIC MODULES VERIFIED & PASSING!")
    print("=" * 60)


if __name__ == "__main__":
    run_tests()
