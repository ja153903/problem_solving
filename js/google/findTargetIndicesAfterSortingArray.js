/**
 * @param {number[]} nums
 * @param {number} target
 * @returns {number[]}
 */
const targetIndices = function (nums, target) {
  nums.sort((a, b) => a - b);

  return nums
    .map((num, index) => ({ num, index }))
    .filter(({ num }) => num === target)
    .map(({ index }) => index);
};
