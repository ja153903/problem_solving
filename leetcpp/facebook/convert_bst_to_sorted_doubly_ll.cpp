class Node {
public:
  int val;
  Node *left;
  Node *right;

  Node() {}

  Node(int _val) {
    val = _val;
    left = nullptr;
    right = nullptr;
  }

  Node(int _val, Node *_left, Node *_right) {
    val = _val;
    left = _left;
    right = _right;
  }
};

/**
 * 426. Convert BST to Sorted Doubly Linked List
 *
 * TODO: I don't understand what this question is asking
 *
 * === Approach ===
 */

class Solution {
public:
  Node *treeToDoublyList(Node *root) {
  }
};
