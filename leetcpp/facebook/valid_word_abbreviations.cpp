#include <iostream>
#include <string>
#include <vector>

/**
 * 408. Valid Word Abbreviation
 *
 * === Approach ===
 *
 */
class Solution {
public:
  bool validWordAbbreviation(std::string word, std::string abbr) {
    int i = 0, j = 0;
    // i will iterate over abbr
    // j will iterate over word

    int current_num = 0;

    while (i < abbr.length() && j < word.length()) {
      if (current_num == 0 && abbr[i] == '0') {
        // this means there is a leading 0
        return false;
      }

      while (abbr[i] >= '0' && abbr[i] <= '9') {
        current_num = current_num * 10 + (abbr[i] - '0');
        i++;
      }

      if (current_num > word.length()) {
        return false;
      }

      if (current_num > 0) {
        for (int k = 0; k < current_num; k++, j++)
          ;
        current_num = 0;
      }

      if (word[j] != abbr[i]) {
        return false;
      }

      j++;
      i++;
    }

    return i >= abbr.length() && j >= word.length();
  }
};

struct TestCase {
public:
  std::string word;
  std::string abbr;
  bool expected;

  TestCase(std::string word, std::string abbr, bool expected)
      : word(word), abbr(abbr), expected(expected) {}
};

int main() {
  Solution s;

  std::vector<TestCase> test_cases;
  test_cases.push_back(TestCase("internationalization", "i12iz4n", true));
  test_cases.push_back(TestCase("apple", "a2e", false));
  test_cases.push_back(TestCase("a", "01", false));
  test_cases.push_back(TestCase("i", "hi1", false));
  test_cases.push_back(TestCase("leetcode", "17", false));

  for (const auto &test_case : test_cases) {
    auto result = s.validWordAbbreviation(test_case.word, test_case.abbr);

    if (result != test_case.expected) {
      std::cout << "Failed test case:" << std::endl;
      std::cout << "word: " << test_case.word << ", abbr: " << test_case.abbr
                << std::endl;
      std::cout << "Expected: " << test_case.expected << ", Actual: " << result
                << std::endl;
      std::cout << std::endl;
    }
  }

  return 0;
}
