/**
 * @param {number} x
 * @param {number} y
 * @return {number}
 */
const hammingDistance = function(x, y) {
  let z = x ^ y;

  let result = 0;

  while (z > 0) {
    if (z & 1 === 1) {
      result += 1;
    }

    z = z >> 1;
  }

  return result;
};
