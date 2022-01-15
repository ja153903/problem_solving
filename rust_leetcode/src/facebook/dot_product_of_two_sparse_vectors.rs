#![allow(dead_code)]

// 1570. Dot Product of Two Sparse Vectors
// 
// === Problem ===
// Given two sparse vectors, compute their dot product
//
// Implement class SparseVector
// * `SparseVector(nums)` initializes the object with the vector `nums`
// * `dotProduct(vec)` computes the dot product between the instances of `SparseVector` and `vec`
//
// === Approach ===
// We can store the index and scalar in the nums vector within a map where the key is the index
// and the value is the scalar within the vector. However we will not store the values that are 0

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

#[cfg(test)]
mod tests {
    use super::SparseVector;

    #[test]
    pub fn test_basic_dot_product() {
        let nums1 = vec![1, 0, 0, 2, 3];
        let nums2 = vec![0, 3, 0, 4, 0];

        let sv1: SparseVector = SparseVector::new(nums1);
        let sv2: SparseVector = SparseVector::new(nums2);

        assert_eq!(sv1.dot_product(sv2), 8);
    }
}
