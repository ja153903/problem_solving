struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

/**
 * 236. Lowest Common Ancestor of a Binary Tree
 *
 * === Approach ===
 * This problem requires us to find some node that is a parent
 * for both p and q (by definition this is what the lca is)
 * However this time we're given the root node
 *
 * if the current root is null, then we return null
 * if the current root is p, then we return p
 * else if the current root is q, then we return q
 * we do this because the lca could be itself
 *
 * then we can iterate down into the left and right subtree
 * if at any point, we do get p and q in the subtree,
 * then we should return the root as the lca
 */

class Solution {
public:
  TreeNode *lowestCommonAncestor(TreeNode *root, TreeNode *p, TreeNode *q) {
    if (root == nullptr) {
      return nullptr;
    }

    if (root == p) {
      return p;
    }

    if (root == q) {
      return q;
    }

    auto left = lowestCommonAncestor(root->left, p, q);
    auto right = lowestCommonAncestor(root->right, p, q);

    if (left && right) {
      return root;
    }

    return left ? left : right;
  }
};
