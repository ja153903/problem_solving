/**
 * 875. Koko Eating Bananas
 *
 * === Problem ===
 * n piles of bananas, ith pile has piles[i] bananas. Guards will come back in h
 * hours each hour she chooses a pile and eats k bananas from that pile. If the
 * pile has less than k bananas, she eats those bananas and thats it for the
 * hour
 *
 * return the minimum integer k such taht she can eat all the bananas within h
 * hours
 */
#include <algorithm>
#include <deque>
#include <iostream>
#include <vector>

class Solution {
public:
  int minEatingSpeed(std::vector<int> &piles, int h) {
    int max_pile = *std::max_element(std::begin(piles), std::end(piles));

    int left = 1, right = max_pile;

    while (left <= right) {
      int hours_spent = 0;
      int mid = left + (right - left) / 2;

      for (const auto &pile : piles) {
        // given k, this will be how many hours it'll take to consume
        // this pile.
        hours_spent += pile / mid;

        // if the remainder of the division is greater than 0
        // then this means there's still left over that will take up
        // another hour
        //
        // ex. if pile = 16 and k = 5, then koko will need to spend
        // an initial 3 hours eating piles of 5 bananas and then
        // an extra hour to eat the last banana
        if (pile % mid != 0) {
          hours_spent++;
        }
      }

      if (hours_spent <= h) {
        right = mid - 1;
      } else {
        left = mid + 1;
      }
    }

    return left;
  }
};

struct TestCase {
public:
  std::vector<int> piles;
  int h;
  int expected;

  TestCase(std::vector<int> piles, int h, int expected)
      : piles(piles), h(h), expected(expected) {}
};

int main() {
  Solution s;

  std::vector<TestCase> test_cases;
  test_cases.push_back(TestCase(std::vector<int>{3, 6, 7, 11}, 8, 4));
  test_cases.push_back(TestCase(std::vector<int>{30, 11, 23, 4, 20}, 5, 30));
  test_cases.push_back(TestCase(std::vector<int>{30, 11, 23, 4, 20}, 6, 23));

  for (auto test_case : test_cases) {
    auto result = s.minEatingSpeed(test_case.piles, test_case.h);

    if (result != test_case.expected) {
      std::cout << "Expected: " << test_case.expected;
      std::cout << ", but got: " << result << std::endl;
    }
  }

  return 0;
}
