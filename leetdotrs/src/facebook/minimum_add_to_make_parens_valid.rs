#![allow(dead_code)]

struct Solution;

// 921. Minimum Add to Make Parentheses Valid
//
// === Problem ===
// Return the minimum number of open or close parentheses you need to add to make the string valid
//
// === Approach ===
// The approach I'm taking is similar to validate parenthesis problem
// except when we hit a closing parens, we check if the stack is empty, then we require an insert
// else we pop for the pair
// we keep doing this until the end, where we return the sum of the required inserts and the length
// of the remaining elements within the stack
impl Solution {
    pub fn min_add_to_make_valid(s: String) -> i32 {
        let mut stack: Vec<char> = Vec::new();
        let mut req_insert: i32 = 0;

        for ch in s.chars() {
            if ch == '(' {
                stack.push(')');
            } else if ch == ')' {
                if stack.is_empty() {
                    req_insert += 1;
                } else {
                    stack.pop();
                }
            }
        }

        req_insert + stack.len() as i32
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    pub fn test_minimum_add() {
        let s = String::from("(((");

        assert_eq!(Solution::min_add_to_make_valid(s), 3);
    }

    #[test]
    pub fn test_minimum_add2() {
        let s = String::from("())");

        assert_eq!(Solution::min_add_to_make_valid(s), 1);
    }

    #[test]
    pub fn test_minimum_add3() {
        let s = String::from("()))((");

        assert_eq!(Solution::min_add_to_make_valid(s), 4);
    }
}
