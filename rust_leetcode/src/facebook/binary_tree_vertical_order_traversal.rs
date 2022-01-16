// 314. Binary Tree Vertical Order Traversal
//
// === Problem ===
// Given the root of a binary tree, return the vertical order traversal of its nodes' values
// (i.e. from top to bottom, column by column)
// 
// If two nodes are in the same row and column, the order should be from left to right
//
// === Approach ===
//
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
use std::collections::HashMap;
use std::rc::Rc;

impl Solution {
    pub fn vertical_order(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<Vec<i32>> {
        let mut map: HashMap<i32, Vec<i32>> = HashMap::new();
        let mut result: Vec<Vec<i32>> = Vec::new();

        Solution::traverse(root, &mut map, 0);

        for (_, &v) in &map {
            result.push(v.to_vec());
        }

        result
    }

    pub fn traverse(root: Option<Rc<RefCell<TreeNode>>>, mp: &mut HashMap<i32, Vec<i32>>, level: i32) {
        if let Some(node) = root {
            if let Some(&mut v) = mp.get(&level) {
                v.push(node.borrow().val);
            } else {
                mp.insert(level, vec![node.borrow().val]);
            }

            Solution::traverse(node.borrow().left.clone(), mp, level - 1);
            Solution::traverse(node.borrow().right.clone(), mp, level + 1);
        }
    }
}
