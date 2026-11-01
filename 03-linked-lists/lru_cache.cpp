/**
 * Problem: LRU Cache (LeetCode #146)
 * Time Complexity: O(1) for get() and put()
 * Space Complexity: O(Capacity)
 */
#include <iostream>
#include <unordered_map>
#include <list>
#include <cassert>

class LRUCache {
private:
    int capacity;
    std::list<std::pair<int, int>> dll; // key, value
    std::unordered_map<int, std::list<std::pair<int, int>>::iterator> cache;

public:
    explicit LRUCache(int cap) : capacity(cap) {}

    int get(int key) {
        auto it = cache.find(key);
        if (it == cache.end()) return -1;
        dll.splice(dll.begin(), dll, it->second);
        return it->second->second;
    }

    void put(int key, int value) {
        auto it = cache.find(key);
        if (it != cache.end()) {
            dll.splice(dll.begin(), dll, it->second);
            it->second->second = value;
            return;
        }
        if (static_cast<int>(dll.size()) >= capacity) {
            int oldKey = dll.back().first;
            dll.pop_back();
            cache.erase(oldKey);
        }
        dll.emplace_front(key, value);
        cache[key] = dll.begin();
    }
};

int main() {
    LRUCache lru(2);
    lru.put(1, 1);
    lru.put(2, 2);
    assert(lru.get(1) == 1);
    lru.put(3, 3);
    assert(lru.get(2) == -1);
    lru.put(4, 4);
    assert(lru.get(1) == -1);
    assert(lru.get(3) == 3);
    assert(lru.get(4) == 4);
    std::cout << "[PASS] LRU Cache C++ Implementation" << std::endl;
    return 0;
}
