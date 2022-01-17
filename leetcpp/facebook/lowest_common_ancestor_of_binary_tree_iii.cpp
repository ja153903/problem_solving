class Node {
public:
  int val;
  Node *left;
  Node *right;
  Node *parent;
};

/**
 * Given two nodes of a binary tree p and q, return their lowest common ancestor (LCA).
 *
 * === Approach ===
 * By definition, what is the lowest common ancestor? The lowest common ancestor is the
 * node that both p and q share as its parent. Also note that the LCA can be itself.
 *
 * The approach here is to work as if this was the list intersection problem.
 * If there is an intersection at any point, then we return that.
 */
class Solution {
public:
  Node *lowestCommonAncestor(Node *p, Node *q) {
    auto a = p;
    auto b = q;

    while (a != b) {
      a = a == nullptr ? q : a->parent;
      b = b == nullptr ? p : b->parent;
    }

    return a;
  }
};
