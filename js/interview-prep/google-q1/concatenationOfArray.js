/**
 * @param {number[]} nums
 * @return {number[]}
 */
function getConcatenation(nums) {
  if (!nums.length) {
    return [];
  }

  return [...nums, ...nums];
}