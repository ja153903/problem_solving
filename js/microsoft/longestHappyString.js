/**
 * @param {number} a
 * @param {number} b
 * @param {number} c
 * @return {string}
 */
const longestDiverseString = function (a, b, c) {
  function helper(a, b, c, aa = "a", bb = "b", cc = "c") {
    if (a < b) {
      return helper(b, a, c, bb, aa, cc);
    }

    if (b < c) {
      return helper(a, c, b, aa, cc, bb);
    }

    if (b === 0) {
      return new Array(Math.min(2, a)).fill(aa).join("");
    }

    const useA = Math.min(2, a);
    const useB = a - useA >= b ? 1 : 0;

    return [
      ...new Array(useA).fill(aa),
      ...new Array(useB).fill(bb),
      ...helper(a - useA, b - useB, c, aa, bb, cc),
    ].join("");
  }

  return helper(a, b, c);
};

console.log(longestDiverseString(1, 1, 7));
console.log(longestDiverseString(7, 1, 0));
console.log(longestDiverseString(2, 4, 1));
