#include <vector>

class Solution {
public:
  bool canPlaceFlowers(std::vector<int> &flowerbed, int n) {
    std::vector<int> candidates;
    int f_size = flowerbed.size();

    if (n == 0) {
      return true;
    }

    if (f_size == 1) {
      return flowerbed[0] == 1 ? false : (n == 1);
    }

    for (int i = 0; i < f_size; i++) {
      if (i == 0) {
        if (flowerbed[i] == 0 && flowerbed[i + 1] == 0) {
          candidates.push_back(i);
        }
      } else if (i == f_size - 1) {
        if (flowerbed[i] == 0 && flowerbed[i - 1] == 0) {
          if (!candidates.empty() && candidates.back() == i - 1) {
            continue;
          }

          candidates.push_back(i);
        }
      } else {
        if (flowerbed[i] == flowerbed[i - 1] &&
            flowerbed[i - 1] == flowerbed[i + 1]) {
          // the only time this is true is the plot is empty
          if (!candidates.empty() && candidates.back() == i - 1) {
            continue;
          }

          candidates.push_back(i);
        }
      }
    }

    return candidates.size() >= n;
  }
};
