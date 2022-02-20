/**
 * @param {number[]} nums
 * @return {number[]}
 */
const sortedSquares = function(nums) {
  return nums.map(num => num * num).sort((a, b) => a - b);
};

// Instead of doing a map and sort,
// we can instead use a two pointer approach
function optimal(nums) {
  const n = nums.length;
  const result = new Array(n).fill(0);
  let i = 0;
  let j = n - 1;

  for (let k = n - 1; k >= 0; k--) {
    if (nums[i] * nums[i] > nums[j] * nums[j]) {
      result[k] = nums[i] * nums[i];
      i++;
    } else {
      result[k] = nums[j] * nums[j];
      j--;
    }
  }

  return result;
}

console.log(optimal([-1, 0, 1, 2, 3]));