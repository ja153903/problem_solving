/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
const targetIndices = function (nums, target) {
  // there might be a better solution here where we keep track of how many items are smaller
  // than the target. Then we also keep track of how many of the target exists
  const result = [];

  let targetCounter = 0;
  let smallerCounter = 0;

  for (let i = 0; i < nums.length; i++) {
    if (nums[i] === target) {
      targetCounter++;
    }

    if (nums[i] < target) {
      smallerCounter++;
    }
  }

  for (let i = smallerCounter; i < smallerCounter + targetCounter; i++) {
    result.push(i);
  }

  return result;
};