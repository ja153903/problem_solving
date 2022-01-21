/**
 * 134. Gas Station
 *
 * There are n gas stations along a circular route where the amount of gas at
 * the ith station is gas[i]
 *
 * You have a car with an unlimited gas tank and it costs cost[i] of gas to
 * travel from the ith station to its next (i + 1)th station. You begin the
 * journey with an empty tank at one of the gas stations.
 *
 * Given two integer arrays gas and cost, return the starting gas station's
 * index if you can travel around the circuit once in the clockwise direction,
 * otherwise return -1. If there exists a solution, it is guaranteed to be
 * unique.
 *
 * === Approach ===
 *
 * We can do an initial pass around to pick candidates for starting indices.
 * Note that we can choose a starting index to be a candidate if gas[i] >=
 * cost[i + 1] Otherwise we wouldnt want to go there. (We can potentially
 * optimize here to say that we should choose the starting index i such that we
 * maximize gas[i] - cost[i + 1])
 */
#include <iostream>
#include <vector>

class Solution {
public:
  int canCompleteCircuit(std::vector<int> &gas, std::vector<int> &cost) {
    int start = 0, total = 0, tank = 0;

    for (int i = 0; i < gas.size(); i++) {
      // starting from the beginning, keep track of total in tank
      // if at any point tank < 0, then this means we should look
      // to the next index to be our start index
      // but at the same time, we should still update our total with the
      // tank value since we're trying to see our total up to that point
      // then we reset the tank value and start again
      tank += gas[i] - cost[i];

      if (tank < 0) {
        start = i + 1;
        total += tank;
        tank = 0;
      }
    }

    // total + tank < 0 means that there is no such starting index
    // that will let us do one circuit
    return total + tank < 0 ? -1 : start;
  }

  int brute_force(std::vector<int> &gas, std::vector<int> &cost) {
    int g = gas.size();
    int c = cost.size();

    if (g != c) {
      return -1;
    }

    std::vector<int> candidate_starting_indices;

    for (int i = 0; i < g; i++) {
      if (gas[i] >= cost[i]) {
        candidate_starting_indices.push_back(i);
      }
    }

    if (candidate_starting_indices.empty()) {
      return -1;
    }

    for (const auto &start : candidate_starting_indices) {
      // go from start -> start + g
      int current_gas = 0;
      bool finished = true;

      for (int i = start; i <= start + g; i++) {
        int actual_idx = i % g;

        current_gas += gas[actual_idx];
        current_gas -= cost[actual_idx];

        if (current_gas < 0) {
          finished = false;
          break;
        }
      }

      if (finished) {
        return start;
      }
    }

    return -1;
  }
};

struct TestCase {
public:
  std::vector<int> gas;
  std::vector<int> cost;
  int expected;

  TestCase(std::vector<int> gas, std::vector<int> cost, int expected)
      : gas(gas), cost(cost), expected(expected) {}
};

int main() {
  Solution s;

  std::vector<TestCase> test_cases;
  test_cases.push_back(TestCase(std::vector<int>{1, 2, 3, 4, 5},
                                std::vector<int>{3, 4, 5, 1, 2}, 3));
  test_cases.push_back(TestCase(std::vector<int>{2, 3, 4},
                                std::vector<int>{3, 4, 3}, -1));

  for (auto test_case : test_cases) {
    auto result = s.canCompleteCircuit(test_case.gas, test_case.cost);
    if (result != test_case.expected) {
      std::cout << "Expected: " << test_case.expected << ", but got: " << result
                << std::endl;
    }
  }

  return 0;
}
