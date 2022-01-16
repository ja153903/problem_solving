#![allow(dead_code)]

struct Solution;

// 1249. Minimum Remove to Make Valid Parenthesis
//
// === Problem ===
// Given a string s of '(' and ')' and lowercase English characters
// Your task is to remove the minimum number of parentheses '(' or ')'
// in any positions so that the resulting parenthesis string is Valid
// and return any valid string.
//
// Formally, a parenthesis string is valid if and only if
// * it is the empty string, containing only lowercase characters, or
// * it can be written as AB (A concatenated with B) where A and B are
//   valid strings, or
// * it can be written as (A), where A is a valid string
//
// === Approach ===
// We can do a pass through the string
// If the character is alphabetic, then we can just add it to the solution
// If the character is an open parenthesis, then we can temporarily add it to our solution
// but we should keep track of its indices in case we need to remove it.
// If the character is a closing parenthesis, then we should keep it if there exists a proper
// pair in the solution,otherwise we should not include it.
// In this solution, we will use '*' as a placeholder!
impl Solution {
    pub fn min_remove_to_make_valid(s: String) -> String {
        let mut result: Vec<char> = Vec::new();
        let mut open_parens: Vec<usize> = Vec::new();

        for (i, ch) in s.chars().enumerate() {
            if ch.is_alphabetic() {
                result.push(ch);
            } else if ch == '(' {
                result.push('*');
                open_parens.push(i);
            } else {
                if let Some(idx) = open_parens.pop() {
                    result[idx] = '(';
                    result.push(')');
                } else {
                    result.push('*');
                }
            }
        }

        result.iter().filter(|&ch| *ch != '*').collect::<String>()
    }
}
