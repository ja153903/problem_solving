/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
const findPairs = function (nums, k) {
  if (nums === null || nums.length <= 1 || k < 0) {
    return 0;
  }

  let result = 0;
  const counter = new Map();

  for (const num of nums) {
    counter.set(num, (counter.get(num) ?? 0) + 1);
  }

  for (const [key, value] of counter) {
    if (k === 0) {
      if (value >= 2) {
        result++;
      }
    } else {
      if (counter.has(key + k)) {
        result++;
      }
    }
  }

  return result;
};

// [1, 1, 3, 4, 5], k = 2
//
console.log(findPairs([3, 1, 4, 1, 5], 2));
console.log(findPairs([1, 2, 3, 4, 5], 1));
console.log(findPairs([1, 3, 1, 5, 4], 0));
