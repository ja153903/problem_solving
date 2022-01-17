#include <iostream>
#include <string>
#include <unordered_map>

#include "../custom_utils.hpp"

class Solution {
public:
  bool wordPattern(std::string pattern, std::string s) {
    std::unordered_map<std::string, std::string> mp;
    auto tokens = leetcode::split_by(s, ' ');

    if (tokens.size() != pattern.length()) {
      return false;
    }

    for (int i = 0; i < pattern.length(); i++) {
      std::string pattern_as_str = std::to_string(pattern[i]);

      auto pattern_to_s = mp.find(pattern_as_str);
      auto s_to_pattern = mp.find(tokens[i]);

      if (pattern_to_s == mp.end() && s_to_pattern == mp.end()) {
        mp[pattern_as_str] = tokens[i];
        mp[tokens[i]] = pattern_as_str;
      } else {
        if (mp[pattern_as_str] != tokens[i] || mp[tokens[i]] != pattern_as_str) {
          return false;
        }
      }
    }

    return true;
  }
};

struct TestCase {
public:
  std::string pattern;
  std::string s;
  bool expected;

  TestCase(std::string pattern, std::string s, bool expected)
      : pattern(pattern), s(s), expected(expected) {}
};

int main() {
  Solution s;

  std::vector<TestCase> test_cases;
  test_cases.push_back(TestCase("abba", "dog cat cat dog", true));
  test_cases.push_back(TestCase("abba", "dog cat cat fish", false));
  test_cases.push_back(TestCase("aaaa", "dog cat cat dog", false));
  test_cases.push_back(TestCase("abba", "dog dog dog dog", false));
  test_cases.push_back(TestCase("aaa", "aa aa aa aa", false));

  for (const auto &test_case : test_cases) {
    auto result = s.wordPattern(test_case.pattern, test_case.s);
    if (result != test_case.expected) {
      std::cout << "For case: (" << test_case.pattern << ", " << test_case.s
                << ") ";
      std::cout << ", we have a failing answer: " << result
                << " when we expected " << test_case.expected << std::endl;
    }
  }

  return 0;
}
