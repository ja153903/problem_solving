#include <vector>

/**
 * 31. Next Permutation
 *
 * === Approach ===
 * According to Wikipedia, here's the algorithm
 * 1. Find the largest index k such that nums[k] < nums[k + 1]. If no such index exists, just reverse nums and done.
 * 2. Find the largest index l > k such that nums[k] < nums[l]
 * 3. Swap nums[k] and nums[l]
 * 4. Reverse the subarray nums[k + 1:]
 */
class Solution {
public:
  void nextPermutation(std::vector<int> &nums) {
    int n = nums.size(), l, k;

    for (k = n - 2; k >= 0; k--) {
      if (nums[k] < nums[k + 1]) {
        break;
      }
    }

    if (k < 0) {
      std::reverse(nums.begin(), nums.end());
    } else {
      for (l = n - 1; l > k; l--) {
        if (nums[l] > nums[k]) {
          break;
        }
      }

      std::swap(nums[k], nums[l]);
      std::reverse(nums.begin() + k + 1, nums.end());
    }
  }
};
