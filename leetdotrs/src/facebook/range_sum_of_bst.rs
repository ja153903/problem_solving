#![allow(dead_code)]

struct Solution;

#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl TreeNode {
    #[inline]
    pub fn new(val: i32) -> Self {
        TreeNode {
            val,
            left: None,
            right: None,
        }
    }
}

use std::cell::RefCell;
use std::rc::Rc;

impl Solution {
    pub fn range_sum_bst(root: Option<Rc<RefCell<TreeNode>>>, low: i32, high: i32) -> i32 {
        if let Some(node) = root {
            let mut sum: i32 = 0;

            let current = node.borrow().val;

            if low <= current && current <= high {
                sum += current;
            }

            if low < current {
                sum += Solution::range_sum_bst(node.borrow().left.clone(), low, high);
            }

            if high > current {
                sum += Solution::range_sum_bst(node.borrow().right.clone(), low, high);
            } 

            return sum
        }

        0
    }
}

