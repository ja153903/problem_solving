#include <unordered_map>
#include <vector>

class Solution {
public:
  int subarraySum(std::vector<int> &nums, int k) {
    std::unordered_map<int, int> mp;
    int cumsum = 0;
    int result = 0;
    mp[0] = 1;

    for (const auto &num : nums) {
      cumsum += num;

      if (mp.find(cumsum - k) != mp.end()) {
        result += mp[cumsum - k];
      }

      if (mp.find(cumsum) == mp.end()) {
        mp[cumsum] = 1;
      } else {
        mp[cumsum] += 1;
      }
    }

    return result;
  }
};
