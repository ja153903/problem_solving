/**
 * 670. Maximum Swap
 *
 * === Problem ===
 * You are given an integer num. You can swap two digits at most once to get the
 * maximum valued number.
 *
 * Return the maximum valued number you can get.
 *
 * === Approach ===
 * What is the greedy approach here? Ideally, we want to make sure that the
 * largest element is at the front. However, if the largest element is already
 * at the front, then we want to make sure that we find the second largest
 * element, etc.
 *
 * I think we can just make the largest swap here.
 */
#include <algorithm>
#include <iostream>
#include <vector>
#include <string>

class Solution {
public:
  std::vector<char> num_to_vector_char(int num) {
    std::vector<char> result;

    while (num > 0) {
      result.push_back('0' + num % 10);
      num /= 10;
    }

    std::reverse(std::begin(result), std::end(result));

    return result;
  }

  int vector_char_to_int(const std::vector<char> &digits) {
    std::string s;

    for (const auto &ch : digits) {
      s.push_back(ch);
    }

    return std::stoi(s);
  }

  int maximumSwap(int num) {
    auto digits = num_to_vector_char(num);
    std::vector<int> bucket(10, 0);

    for (int i = 0; i < digits.size(); i++) {
      bucket[digits[i] - '0'] = i;
    }

    for (int i = 0; i < digits.size(); i++) {
      for (int j = 9; j > digits[i] - '0'; j--) {
        if (bucket[j] > i) {
          std::swap(digits[i], digits[bucket[j]]);
          return vector_char_to_int(digits);
        }
      }
    }

    return num;
  }
};

int main() {
  Solution s;

  std::cout << s.maximumSwap(2736) << std::endl;

  return 0;
}
