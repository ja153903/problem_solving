/**
 * @param {number} x
 * @param {number} y
 * @return {number}
 */
const hammingDistance = function (x, y) {
  let result = 0;
  // DO the XOR operation
  let n = x ^ y;

  while (n > 0) {
    result++;
    // n & (n-1) converts the right most 1 to 0.
    // so for this problem we continuously do this
    // until we have 0
    n &= n - 1;
  }

  return result;
};