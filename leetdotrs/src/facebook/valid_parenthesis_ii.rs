#![allow(dead_code)]

struct Solution;

// 680. Valid Palindrome II
//
// === Problem ===
// Given a string s, return true if the s can be a palindrome after deleting
// at most one character from it
//
// === Approach ===
// The approach for this problem should be to use two pointers
// We compare front and back pointers.
// if at any point the front and back pointers are not equal there are two ways we can delete
// we can either omit the front pointer or we can omit the back pointer
impl Solution {
    pub fn valid_palindrome(s: String) -> bool {
        let mut i: i32 = 0;
        let mut j: i32 = (s.len() as i32) - 1;

        while i < j {
            let ui = i as usize;
            let uj = j as usize;

            if s[ui..ui+1] != s[uj..uj + 1] {
                return Solution::is_palindrome(&s, i + 1, j) || Solution::is_palindrome(&s, i, j - 1);
            }

            i += 1;
            j -= 1;
        }

        true
    }

    pub fn is_palindrome(s: &str, mut i: i32, mut j: i32) -> bool {
        while i < j {
           let ui = i as usize;
            let uj = j as usize;

            if s[ui..ui+1] != s[uj..uj + 1] {
                return false;
            }

            i += 1;
            j -= 1;
        }

        true
    }
} 
