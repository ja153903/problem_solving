#![allow(dead_code)]

// 938. Range Sum of BST
//
// === Problem ===
// Given the root node of a binary search tree and two integers low and high
// return the sum of the values of all nodes with a value in the inclusive range [low, high]
//
// === Approach ===
// We can just go over all the nodes and return the sum as long as its within the range
// Note that when working with Rc<RefCell<TreeNode>>>, we'll want to use the borrow method

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

struct Solution;

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

            sum
        } else {
            0
        }
    }
}
