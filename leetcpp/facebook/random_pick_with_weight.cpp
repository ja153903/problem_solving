#include <vector>

class Solution {
private:
  std::vector<int> cumsum;
public:
    Solution(std::vector<int>& w) {
      int acc = 0;

      for (int i = 0; i < w.size(); i++) {
        acc += w[i];
        cumsum.push_back(acc);
      }
    }
    
    int pickIndex() { 
      int n = rand() % cumsum.back() + 1;
      auto it = std::lower_bound(cumsum.begin(), cumsum.end(), n);
      return it - cumsum.begin();
    }
};

