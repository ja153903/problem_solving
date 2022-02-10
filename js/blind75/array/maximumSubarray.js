/**
 * At this point this is a trivia problem.
 * Solution is Kadane's algorithm
 *
 * @param {number[]} nums
 * @return {number}
 */
function maxSubArray(nums) {
  if (!nums || !nums.length) {
    return 0;
  }

  let maxSoFar = nums[0];
  let currentMax = nums[0];

  for (let i = 1; i < nums.length; i++) {
    maxSoFar = Math.max(nums[i], maxSoFar + nums[i]);
    currentMax = Math.max(currentMax, maxSoFar);
  }

  return currentMax;
}
