/**
 * Honestly it's like maximum subarray except
 * that we also keep track of minimum because
 * product of negative numbers can potentially be the max product
 *
 * @param {number[]} nums
 * @return {number}
 */
function maxProduct(nums) {
  // keep track of maxSoFar and minSoFar
  let maxSoFar = nums[0];
  let minSoFar = nums[0];
  let max = nums[0];

  for (let i = 1; i < nums.length; i++) {
    // store minSoFar in temp variable
    const tempMin = minSoFar;

    // update minSoFar if possible
    minSoFar = Math.min(nums[i], nums[i] * minSoFar, nums[i] * maxSoFar);

    // update maxSoFar if possible
    maxSoFar = Math.max(nums[i], nums[i] * tempMin, nums[i] * maxSoFar);

    // update max if possible
    max = Math.max(max, maxSoFar);
  }

  return max;
}

let nums = [2, 3, -2, 4];

console.log(maxProduct(nums));

nums = [-2, 0, -1];

console.log(maxProduct(nums));
