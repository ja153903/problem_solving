#include <vector>
#include <queue>

/**
 * 215. Kth largest element in array
 *
 * === Approach ===
 * The idea here is to use a priority queue (where we keep track of the largest elements)
 */
class Solution {
public:
  int findKthLargest(std::vector<int> &nums, int k) {
    std::priority_queue<int> pq(nums.begin(), nums.end());

    for (int i = 0; i < k - 1; i++) {
      pq.pop();
    }

    return pq.top();
  }
};
