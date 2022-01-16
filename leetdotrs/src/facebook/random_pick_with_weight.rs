#![allow(dead_code)]

// 528. Random Pick with Weight
//
// === Problem ===
// You are given a 0-indexed array of positive integers w where w[i] describes the weight of the
// ith index.
//
// You need to implement the function pickIndex() which randomly picks an index in the range [0,
// w.length - 1] and returns it. The probability of picking an index i is w[i] / sum(w)
//
// === Approach ===
// The approach we're likely to use here is to use some form of uniform random sampling
// by extending the weights to be ranges. So for example, if we have an array of weights [1, 3]
// we can transform this to be an array of weights [1, 4] s.t. when we randomly generate numbers,
// numbers less than
//
// TODO: Should look up on what the BTreeMap actually provides us as a performance improvement
//
use rand::Rng;
use std::collections::BTreeMap;

struct Solution {
    btm: BTreeMap<i32, usize>,
    max_weight: i32,
}

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl Solution {
    fn new(w: Vec<i32>) -> Self {
        let mut btm: BTreeMap<i32, usize> = BTreeMap::new();
        let mut max_weight: i32 = 0;

        for &weight in w.iter() {
            max_weight += weight;
            btm.insert(max_weight, btm.len());
        }

        Self { btm, max_weight }
    }

    fn pick_index(&self) -> i32 {
        let mut rng = rand::thread_rng();
        let pick: i32 = rng.gen_range(0..self.max_weight);

        if let Some(next) = self.btm.range(pick + 1..).next() {
            *next.1 as i32
        } else {
            -1
        }
    }
}
