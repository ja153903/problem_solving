#include <vector>
#include <unordered_map>

class SparseVector {
private:
  std::unordered_map<int, int> mp;
public:
  SparseVector(std::vector<int> &nums) {
    for (int i = 0; i < nums.size(); i++) {
      if (nums[i] != 0) {
        mp[i] = nums[i];
      }
    }
  }

  // Return the dotProduct of two sparse vectors
  int dotProduct(SparseVector &vec) {
    int result = 0;

    for (const auto &[key, value]: mp) {
      if (vec.mp.find(key) != vec.mp.end()) {
        result += value * vec.mp[key];
      }
    }

    return result;
  }
};
