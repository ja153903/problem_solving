#![allow(dead_code)]

struct Solution;

// 560. Subarray Sum Equals K
//
// === Problem ===
//
// Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.
//
// === Approach ===
//
// We can continuously add the numbers that we see. We will continuously add the sum we find some
// hashmap.
use std::collections::HashMap;

impl Solution {
    pub fn subarray_sum(nums: Vec<i32>, k: i32) -> i32 {
        let mut map: HashMap<i32, i32> = HashMap::new();
        let mut cumsum: i32 = 0;
        let mut result: i32 = 0;

        map.insert(0, 1);

        for &num in nums.iter() {
            cumsum += num;

            if map.contains_key(&(cumsum - k)) {
                result += map.get(&(cumsum - k)).unwrap_or(&0);
            }

            // insert or update based on the cumsum
            map.insert(cumsum, map.get(&cumsum).unwrap_or(&0) + 1);
        }

        result
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    pub fn test_subarray_sum() {
        let nums = vec![1, 1, 1];
        let k = 2;

        assert_eq!(Solution::subarray_sum(nums, k), 2);
    }

    #[test]
    pub fn test_subarray_sum2() {
        let nums = vec![1, 2, 3];
        let k = 3;

        assert_eq!(Solution::subarray_sum(nums, k), 2);
    }

    #[test]
    pub fn test_subarray_sum3() {
        let nums = vec![1, -1, 0];
        let k = 0;

        assert_eq!(Solution::subarray_sum(nums, k), 3);
    }
}
