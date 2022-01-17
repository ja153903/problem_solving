#include <algorithm>
#include <cassert>
#include <iostream>
#include <utility>
#include <vector>

typedef std::pair<std::vector<int>, std::vector<int>> TestCase;

class Solution {
public:
  std::vector<int> findBuildings(std::vector<int> &heights) {
    std::vector<int> res;

    int local_max = heights[heights.size() - 1];

    res.push_back(heights.size() - 1);

    for (int i = heights.size() - 2; i >= 0; i--) {
      if (heights[i] > local_max) {
        local_max = heights[i];
        res.push_back(i);
      }
    }

    std::reverse(std::begin(res), std::end(res));

    return res;
  }
};

int main() {
  Solution s;

  std::vector<TestCase> test_cases;
  test_cases.push_back(
      std::make_pair(std::vector<int>{4, 2, 3, 1}, std::vector<int>{0, 2, 3}));

  for (auto c : test_cases) {
    auto res = s.findBuildings(c.first);
    assert(res == c.second);
  }

  return 0;
}
