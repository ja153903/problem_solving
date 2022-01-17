#![allow(dead_code)]

struct Solution;

// 849. Maximize Distance to Closest Person
//
// === Approach ===
// The idea with this solution is to consider the indices where there exists a person sitting
// at each point, we can then compare the distance between this person sitting to the last time
// we saw a person sitting and compute half the distance from each of those indices where we found
// people sitting. This gives us a distance to insert a new person and we try to maximize this.
//
// At the end, we compare the max of the result we've been tabulating to the distance of the last
// time we saw a person sitting in reference to the entire array (this is the case where the person
// sitting is located near the front of the array; not that we handle the case where the person is
// at the edge within loop itself, but we do not take care of the case where the person is at the
// beginning of the array)

use std::cmp;

impl Solution {
    pub fn max_dist_to_closest(seats: Vec<i32>) -> i32 {
        let n = seats.len();
        let mut res: i32 = 0;
        let mut last: i32 = -1;

        for (i, &val) in seats.iter().enumerate() {
            if val > 0 {
                let candidate: i32 = if last < 0 {
                    i as i32
                } else {
                    (i as i32 - last) / 2
                };
                res = cmp::max(res, candidate);
                last = i as i32;
            }
        }

        cmp::max(res, (n as i32) - last - 1)
    }

    pub fn failed_solution(seats: Vec<i32>) -> i32 {
        let n = seats.len();

        let idxs: Vec<usize> = seats
            .iter()
            .enumerate()
            .filter(|(_, &val)| val == 1)
            .map(|(i, _)| i)
            .collect();
        let m = idxs.len();

        if m == 1 {
            return cmp::max((n - idxs[0] - 1) as i32, idxs[0] as i32);
        }

        let mut max_diff: i32 = idxs[0] as i32;

        for i in 1..m {
            max_diff = cmp::max(max_diff, (idxs[i] - idxs[i - 1]) as i32 / 2);
        }

        max_diff
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    pub fn test_max_dist_to_closest() {
        let seats = vec![1, 0, 0, 0];
        assert_eq!(Solution::max_dist_to_closest(seats), 3);
    }

    #[test]
    pub fn test_max_dist_to_closest2() {
        let seats = vec![1, 0, 0, 0, 1, 0, 1];
        assert_eq!(Solution::max_dist_to_closest(seats), 2);
    }

    #[test]
    pub fn test_max_dist_to_closest3() {
        let seats = vec![0, 1];
        assert_eq!(Solution::max_dist_to_closest(seats), 1);
    }

    #[test]
    pub fn test_max_dist_to_closest4() {
        let seats = vec![0, 0, 1, 0, 1, 1];
        assert_eq!(Solution::max_dist_to_closest(seats), 2);
    }
}
