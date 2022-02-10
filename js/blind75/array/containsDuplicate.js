/**
 * Contains Duplicate wants us to return true if some value occurs more than once
 * else we return false.
 *
 * @param {number[]} nums
 * @return {boolean}
 */
function containsDuplicate(nums) {
  // use set to keep track of seen values
  const seen = new Set();

  for (const num of nums) {
    // if value already exists in set, return true
    if (seen.has(num)) {
      return true;
    }

    // add to set if unique
    seen.add(num);
  }

  // if we get here, then that means there is no duplicate
  return false;
}
