/**
 * @param {number[]} nums
 * @return {boolean}
 */
const uniqueOccurrences = function(nums) {
  const counter = new Map();

  for (const num of nums) {
    counter.set(num, (counter.get(num) ?? 0) + 1);
  }

  const uniqueCount = new Set();

  for (const value of counter.values()) {
    if (uniqueCount.has(value)) {
      return false;
    }

    uniqueCount.add(value);
  }

  return true;
};