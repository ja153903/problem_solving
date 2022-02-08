/**
  * The intuition behind this problem is to use the 
  * assumption that a >= b >= c
  * This assumption simplifies our approach
  * as the idea is that we take 2 of characters from the largest bucket
  * and append them to our result string. Every time we find that
  * our largest bucket has changed, we recursively call the function with
  * the values swapped as to provide the necessary cushion
  * if our medium value b is empty, then this means we can add the rest of the largest value
  * available in a
  *
  * otherwise, we need to make sure that we provide 2 of the largest value and a buffer value of 
  * b in the middle then recursively search for more values to introduce into the result string.
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
