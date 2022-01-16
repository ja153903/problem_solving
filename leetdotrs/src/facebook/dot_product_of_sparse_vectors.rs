#![allow(dead_code)]

use std::collections::HashMap;

struct SparseVector {
    repr: HashMap<usize, i32>
}

impl SparseVector {
    fn new(nums: Vec<i32>) -> Self {
        let mut repr: HashMap<usize, i32> = HashMap::new();
        for (i, &val) in nums.iter().enumerate() {
            if val != 0 {
                repr.insert(i, val);
            }
        }

        Self {
            repr
        }
    }

    fn dot_product(&self, vec: SparseVector) -> i32 {
        let mut result = 0;

        for (key, value) in &self.repr {
            if vec.repr.contains_key(key) {
                let other_value = vec.repr.get(key);
                result += value * other_value.unwrap();
            }
        }

        result
    }
}
