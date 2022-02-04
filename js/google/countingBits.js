/**
 * @param {number} n
 * @return {number[]}
 */
const countBits = function (n) {
  const result = [];

  for (let i = 0; i <= n; i += 1) {
    result.push(getNumBits(i));
  }

  return result;
};

/**
  * @param {number} n
  * @returns {number}
  */
function getNumBits(n) {
  let result = 0;

  while (n > 0) {
    if (n & 1 === 1) {
      result += 1;
    }

    n = n >> 1;
  }

  return result;
}

console.log(countBits(2));
