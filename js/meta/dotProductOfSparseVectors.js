class SparseVector {
  /**
   * @param {number[]} nums
   */
  constructor(nums) {
    this.sparseMap = new Map();

    for (let i = 0; i < nums.length; i++) {
      if (nums[i] !== 0) {
        this.sparseMap.set(i, nums[i]);
      }
    }
  }

  /**
   * Return the dot product of two sparse vectors
   * @param {SparseVector} vec
   * @return {number}
   */
  dotProduct(vec) {
    let result = 0;

    for (const [key, value] of this.sparseMap.entries()) {
      if (vec.sparseMap.has(key)) {
        result += value * vec.sparseMap.get(key);
      }
    }

    return result;
  }
}

function main() {
  const sv1 = new SparseVector([1, 0, 0, 2, 3]);
  const sv2 = new SparseVector([0, 3, 0, 4, 0]);

  console.log(sv1.dotProduct(sv2));
}

main();
