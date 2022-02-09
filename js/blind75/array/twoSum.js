/**
 * Two Sum asks us to find two indices within the array
 * such that the sum of the values at those indices add up to
 * a target value.
 *
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
function twoSum(nums, target) {
  // Use a hashmap to keep track of numbers we've seen as the key
  // and the index we saw the value at as the value.
  const seen = new Map();

  for (let i = 0; i < nums.length; i++) {
    if (seen.has(target - nums[i])) {
      // if the difference between the target and the current number
      // is in the map, then this means we can construct a pair of values
      // nums[i] and nums[j] such that nums[i] + nums[j] === target
      return [seen.get(target - nums[i]), i];
    }

    // if target - nums[i] is not in the map currently,
    // then we should set the current value and its index in the map
    seen.set(nums[i], i);
  }

  // if no such pair of indices exists, then we should return an empty array
  return [];
}
