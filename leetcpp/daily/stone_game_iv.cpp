/**
 * 1510. Stone Game IV
 *
 * === Problem ===
 * Alice and Bob take turns playing a game, with Alice starting first.
 *
 * Initially, there are n stones in a pile. On each player's turn, that player
 * makes a move consisting of removing any non-zero square number of stones in
 * the pile.
 *
 * Also, if a player cannot make a move, he/she loses the game
 *
 * Given a positive integer n, return true if and only if Alice wins the game
 * otherwise return false, assuming both players play optimally.
 *
 * === Approach ===
 * dp[i] ~ can you win at n = i
 *
 * If there exists a k such that dp[i - k * k] == false, then dp[i] = true
 * Why is this so? If there exists a move such that we can take a square number
 * while the previous move before that is false, then we win! (note that the
 * previous move being false means that your opponent can't win on that move)
 */
#include <vector>

class Solution {
public:
  bool winnerSquareGame(int n) {
    std::vector<bool> dp(n + 1);

    for (int i = 1; i <= n; i++) {
      for (int k = 1; k * k <= i; k++) {
        if (!dp[i - k * k]) {
          dp[i] = true;
          break;
        }
      }
    }

    return dp[n];
  }
};
