struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode() : val(0), left(nullptr), right(nullptr) {}
  TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
  TreeNode(int x, TreeNode *left, TreeNode *right)
      : val(x), left(left), right(right) {}
};

#include <vector>
#include <queue>

/**
 * 199. Binary Tree Right Side View
 *
 * === Approach ===
 * We can use level order traversal for this problem
 */
class Solution {
public:
  std::vector<int> rightSideView(TreeNode *root) {
    if (root == nullptr) {
      return {};
    }

    std::vector<int> result;
    std::queue<TreeNode *> q;
    q.push(root);

    while (!q.empty()) {
      int q_size = q.size();

      for (int i = 0; i < q_size; i++) {
        auto front = q.front();
        q.pop();

        if (i == q_size - 1) {
          result.push_back(front->val);
        }

        if (front->left != nullptr) {
          q.push(front->left);
        }

        if (front->right != nullptr) {
          q.push(front->right);
        }
      }
    }

    return result;
  }
};
