/**
 * @param {number[]} nums
 * @return {number[]}
 */
const sortArrayByParity = function(nums) {
  // even first then odd
  const even = [];
  const odd = [];

  for (const num of nums) {
    if (num % 2 === 0) {
      even.push(num);
    } else {
      odd.push(num);
    }
  }

  return [...even, ...odd];
};