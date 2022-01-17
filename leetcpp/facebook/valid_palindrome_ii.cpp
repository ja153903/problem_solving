#include <iostream>
#include <string>
#include <vector>

class Solution {
public:
  bool validPalindrome(std::string s) {
    int i = 0, j = s.length() - 1;

    while (i < j) {
      if (s[i] != s[j]) {
        return is_palindrome(s, i + 1, j) || is_palindrome(s, i, j - 1);
      }
      i++;
      j--;
    }

    return true;
  }

  bool is_palindrome(std::string s, int i, int j) {
    while (i < j) {
      if (s[i] != s[j]) {
        return false;
      }
      i++;
      j--;
    }

    return true;
  }
};

int main() {
  Solution s;
  bool passes_all_cases = true;

  std::vector<std::pair<std::string, bool>> test_cases;
  test_cases.push_back(std::make_pair("aba", true));
  test_cases.push_back(std::make_pair("abca", true));
  test_cases.push_back(std::make_pair("abc", false));

  for (const auto &c : test_cases) {
    auto result = s.validPalindrome(c.first);

    if (result != c.second) {
      passes_all_cases = false;
      std::cout << "Failed test case with input: " << c.first << std::endl;
      std::cout << "Produced the following: " << result << std::endl;
    }
  }

  if (passes_all_cases) {
    std::cout << "All cases passed" << std::endl;
  }

  return 0;
}
