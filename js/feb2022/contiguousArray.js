/**
 * The idea behind this solution is that we know we're at an even number
 * of ones and zeros if the current sum is equal to 0 if we add 1 if the value
 * is one and subtract one if the value is zero.
 *
 * So as we iterate, we want to keep track of various counts we achieve and store
 * those counts. If we contain such a count, this means that we can create a contiguous subarray
 * as we've created the second half of some other subarray
 *
 * @param {number[]} nums
 * @return {number}
 */
const findMaxLength = function (nums) {
  let count = 0;
  let max = 0;

  const dict = new Map();
  dict.set(0, 0);

  for (let i = 0; i < nums.length; i++) {
    if (nums[i] === 1) {
      count++;
    } else {
      count--;
    }

    if (dict.has(count)) {
      max = Math.max(max, i - dict.get(count) + 1);
    } else {
      dict.set(count, i + 1);
    }
  }

  return max;
};

/**
 * @param {number[]} nums
 * @returns {number}
 */
const bruteForce = function (nums) {
  let max = 0;
  for (let i = 0; i < nums.length; i++) {
    let zeros = 0;
    let ones = 0;

    for (let j = i; j < nums.length; j++) {
      if (nums[j] === 1) {
        ones++;
      } else {
        zeros++;
      }

      if (ones === zeros) {
        max = Math.max(max, zeros + ones);
      }
    }
  }

  return max;
};

console.log(bruteForce([0, 1]));
console.log(findMaxLength([0, 1]));
console.log(findMaxLength([0, 1, 0]));
