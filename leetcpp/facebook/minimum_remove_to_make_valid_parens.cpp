#include <iostream>
#include <string>
#include <vector>

class Solution {
public:
  std::string minRemoveToMakeValid(std::string s) {
    std::vector<char> scan(s.length());
    std::vector<int> indices;

    for (auto i = 0; i < s.length(); i++) {
      if (s[i] != '(' && s[i] != ')') {
        // i.e. this is going to be alphabetic
        scan[i] = s[i];
      } else if (s[i] == '(') {
        scan[i] = '*';
        indices.push_back(i);
      } else {
        if (indices.empty()) {
          scan[i] = '*';
        } else {
          int last = indices.back();
          scan[i] = ')';
          scan[last] = '(';

          indices.pop_back();
        }
      }
    }

    std::string res;

    for (const auto &ch : scan) {
      if (ch != '*') {
        res.push_back(ch);
      }
    }

    return res;
  }
};

int main() {
  Solution s;
  bool passes_all_cases = true;

  std::vector<std::pair<std::string, std::string>> test_cases;
  test_cases.push_back(std::make_pair("lee(t(c)o)de)", "lee(t(c)o)de"));
  test_cases.push_back(std::make_pair("a)b(c)d", "ab(c)d"));
  test_cases.push_back(std::make_pair("))((", ""));

  for (const auto &c : test_cases) {
    auto result = s.minRemoveToMakeValid(c.first);

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
