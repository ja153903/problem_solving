#include <string>
#include <vector>
#include <sstream>

namespace leetcode {
  std::vector<std::string> split_by(std::string s, char delim) {
    std::vector<std::string> tokens;
    std::stringstream strm(s);
    std::string tmp;

    while (std::getline(strm, tmp, delim)) {
      tokens.push_back(tmp);
    }

    return tokens;
  }
};
