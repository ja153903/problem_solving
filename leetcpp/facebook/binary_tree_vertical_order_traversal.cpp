struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode() : val(0), left(nullptr), right(nullptr) {}
  TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
  TreeNode(int x, TreeNode *left, TreeNode *right)
      : val(x), left(left), right(right) {}
};

#include <map>
#include <queue>
#include <vector>

class Solution {
public:
  std::vector<std::vector<int>> verticalOrder(TreeNode *root) {
    if (root == nullptr) {
      return {};
    }

    std::vector<std::vector<int>> res;
    std::map<int, std::vector<int>> mp;
    std::queue<std::pair<TreeNode *, int>> q;

    q.push(std::make_pair(root, 0));

    while (!q.empty()) {
      auto front = q.front();
      q.pop();

      mp[front.second].push_back(front.first->val);

      if (front.first->left != nullptr) {
        q.push(std::make_pair(front.first->left, front.second - 1));
      }

      if (front.first->right != nullptr) {
        q.push(std::make_pair(front.first->right, front.second + 1));
      }
    }

    for (const auto &[_key, value] : mp) {
      res.push_back(value);
    }

    return res;
  }
};
