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

  // get a frequency of all the values in the list
  for (const num of nums) {
    counter.set(num, (counter.get(num) ?? 0) + 1);
  }

  // go over each key
  for (const [key, value] of counter) {
    // if k is 0, then we should count all the unique pairs
    // of values
    if (k === 0) {
      if (value >= 2) {
        result++;
      }
    } else {
      // if k is greater than 0, then we should check if
      // the current key + k is in the map
      // because if it exists, then we have the pair
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
