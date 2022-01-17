#include <string>
#include <stack>

class Solution {
public:
    int minAddToMakeValid(std::string s) {
      if (s.empty()) {
        return 0;
      }

      int result = 0;

      std::stack<char> stk;

      for (const auto &ch : s) {
        if (ch == '(') {
          stk.push('(');
        } else if (ch == ')') {
          if (stk.empty()) {
            result++;
          } else {
            stk.pop();
          }
        }
      }

      return result + stk.size();
    }
};
