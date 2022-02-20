/**
 * @param {number} n
 * @return {number[]}
 */
const countBits = function(n) {
  const dp = new Array(n + 1).fill(0);

  for (let i = 1; i <= n; i++) {
    // dp[i] depends on the state of the number bit shifted
    // to the right and if the right most bit is a 1
    dp[i] = dp[i >> 1] + ((i & 1) === 1 ? 1 : 0);
  }

  return dp;
};