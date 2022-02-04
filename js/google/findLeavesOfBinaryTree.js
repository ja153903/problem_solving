class TreeNode {
    constructor(val, left, right) {
        this.val = val ?? 0;
        this.left = left ?? null;
        this.right = right ?? null;
    }
}

/**
 * @param {TreeNode} root
 * @returns {number[][]}
 */
const findLeaves = function (root) {
  const result = [];

  depth(root, result);

  return result;
};

/**
  * @param {TreeNode} root
  * @param {number[][]} result
  * @returns {number}
  */
function depth(root, result) {
  if (!root) {
    // we return -1 because our base level should be 0-indexed
    return -1;
  }

  // grab the depth 
  const leftSubtreeDepth = depth(root.left, result);
  const rightSubtreeDepth = depth(root.right, result);

  root.left = null;
  root.right = null;

  const level = 1 + Math.max(leftSubtreeDepth, rightSubtreeDepth);

  if (result.length === level) {
    result.push([]);
  }

  // the depth is the key we're using if they have the same depth
  // then they should be on the same level
  result[level].push(root.val);

  return level;
}
