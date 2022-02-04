/**
 * @param {number[]} nums
 * @return {number[]}
 */
function getConcatenation(nums) {
  return [...nums, ...nums];
}

console.log(getConcatenation([1, 2, 3]));
