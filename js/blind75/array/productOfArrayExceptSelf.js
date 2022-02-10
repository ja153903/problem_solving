/**
 * Given an integer array nums, return an array answer such that answer[i]
 * is equal to the product of all the elements of nums except nums[i].
 * The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 * You must write an algorithm that runs in O(n) time and without using the division operation.
 *
 * @param {number[]} nums
 * @return {number[]}
 */
function productExceptSelf(nums) {
  const result = new Array(nums.length).fill(1);

  for (let i = 1; i < nums.length; i++) {
    result[i] = result[i - 1] * nums[i - 1];
  }

  let right = 1;

  for (let j = nums.length - 1; j >= 0; j--) {
    result[j] *= right;
    right *= nums[j];
  }

  return result;
}
