#include <string>
#include <stack>

class Solution {
public:
  std::string simplifyPath(std::string path) {
    std::stack<std::string> stk;

    int i = 0;

    while (i < path.length()) {
      while (i < path.length() && path[i] == '/') {
        i++;
      }

      std::string tmp;

      while (i < path.length() && path[i] != '/') {
        tmp += path[i];
        i++;
      }

      if (!stk.empty() && tmp == "..") {
        stk.pop();
      }

      if (tmp != "." && tmp != "..") {
        stk.push(tmp);
      }

      i++;
    }

    std::string s;

    while (!stk.empty()) {
      auto top = stk.top();
      stk.pop();

      if (s.empty()) {
        s = top + s;
      } else {
        s = top + "/" + s;
      }
    }

    return "/" + s;
  }
};
