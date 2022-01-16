#![allow(dead_code, unused_comparisons)]

struct Solution;

// 1762. Buildings with an Ocean View
//
// === Problem ===
// There are n buildings in a line. You are given an integer array heights of size n
// that represent the heights of the buildings in the line.
//
// The ocean is to the right of the buildings. A building has an ocean view if the building
// can see the ocean without obstructions. Formally, a building has an ocean view if all
// the buildings to its right have a smaller height.
//
// Return a list of indices (0-indexed) of buildings that have an ocean view,
// sorted in increasing order.
//
// === Approach ===
// The idea here is that we want to go from the last index and work our way backwards.
// We want to incrementally update the local_max
impl Solution {
    pub fn find_buildings(heights: Vec<i32>) -> Vec<i32> {
        if heights.is_empty() {
            return Vec::new();
        }

        if heights.len() == 1 {
            return vec![0];
        }

        let mut i = heights.len() - 1;
        let mut local_max = heights[i];
        let mut result: Vec<i32> = Vec::new();

        result.push(i as i32);
        i -= 1;
        
        while i >= 0 {
            if heights[i] > local_max {
                result.push(i as i32);
                local_max = heights[i];
            }

            if i == 0 {
                break;
            } else {
                i -= 1;
            }
        }

        result.into_iter().rev().collect()
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    pub fn test_basic_case() {
        let heights = vec![4, 2, 3, 1];
        assert_eq!(Solution::find_buildings(heights), vec![0, 2, 3]);
    }

    #[test]
    pub fn test_basic_case2() {
        let heights = vec![4, 3, 2, 1];
        assert_eq!(Solution::find_buildings(heights), vec![0, 1, 2, 3]);
    }

    #[test]
    pub fn test_basic_case3() {
        let heights = vec![1, 3, 2, 4];
        assert_eq!(Solution::find_buildings(heights), vec![3]);
    }

    #[test]
    pub fn test_basic_case4() {
        let heights = vec![44];
        assert_eq!(Solution::find_buildings(heights), vec![0]);
    }
}
