#![allow(dead_code)]

struct Solution;

// Definition for a binary tree node.
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

// 314. Binary Tree Vertical Order Traversal
//
// === Approach ===
// The approach with this problem is to modify a level order traversal
// while keeping track of the horizontal level with which each node spreads
// these values are then kept track within a hashmap and returned as such
//
// This implementation requires us to use a BTreeMap to make sure that the
// map is sorted inherently
use std::cell::RefCell;
use std::collections::{BTreeMap, VecDeque};
use std::rc::Rc;

struct QueueNode {
    node: Option<Rc<RefCell<TreeNode>>>,
    level: i32,
}

impl Solution {
    pub fn vertical_order(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<Vec<i32>> {
        let mut queue: VecDeque<QueueNode> = VecDeque::new();
        let mut mp: BTreeMap<i32, Vec<i32>> = BTreeMap::new();

        if root.is_none() {
            return vec![];
        }

        queue.push_back(QueueNode {
            node: root,
            level: 0,
        });

        while !queue.is_empty() {
            let q_node = queue.pop_front();
            if let Some(q_node) = q_node {
                let QueueNode { node, level } = q_node;

                if let Some(node) = node {
                    if let Some(v) = mp.get_mut(&level) {
                        v.push(node.borrow().val);
                    } else {
                        mp.insert(level, vec![node.borrow().val]);
                    }

                    queue.push_back(QueueNode {
                        node: node.borrow().left.clone(),
                        level: level - 1,
                    });
                    queue.push_back(QueueNode {
                        node: node.borrow().right.clone(),
                        level: level + 1,
                    });
                }
            }
        }

        let mut result: Vec<Vec<i32>> = Vec::new();

        for (_, value) in &mp {
            result.push(value.to_vec());
        }

        result
    }
}
