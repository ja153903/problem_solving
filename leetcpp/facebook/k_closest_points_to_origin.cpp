#include <vector>
#include <queue>

typedef std::vector<int> Point;
typedef std::vector<Point> Points;

class CustomComparator {
public:
  bool operator() (const Point &p1, const Point &p2) {
    auto p1_dist = p1[0] * p1[0] + p1[1] * p1[1];
    auto p2_dist = p2[0] * p2[0] + p2[1] * p2[1];

    return p1_dist < p2_dist;
  }
};

class Solution {
public:
  Points kClosest(Points &points, int k) {
    Points res;
    std::priority_queue<Point, Points, CustomComparator> pq;

    for (const auto &point : points) {
      pq.push(point);

      if (pq.size() == k + 1) {
        pq.pop();
      }
    }

    while (!pq.empty()) {
      res.push_back(pq.top());
      pq.pop();
    }

    return res;
  }
};
