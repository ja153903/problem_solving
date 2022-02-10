/**
 * @param {number[]} nums
 * @return {number}
 */
function findMin(nums) {
  let left = 0;
  let right = nums.length - 1;

  while (left < right) {
    const mid = Math.floor((left + right) / 2);

    // if the number in the middle is greater than
    // the number on the right
    if (nums[mid] > nums[right]) {
      left = mid + 1;
    } else {
      right = mid;
    }
  }

  return nums[left];
}

// Solution Notes:
// Brute Force solution here is a linear scan.
// Given that the array is sorted, we want to make sure
// that we use binary search for an optimal solution
