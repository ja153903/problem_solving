struct ListNode {
  int val;
  ListNode *next;
  ListNode(int x) : val(x), next(nullptr) {}
};

#include <unordered_set>

class Solution {
public:
  ListNode *detectCycle(ListNode *head) {
    std::unordered_set<ListNode *> seen;

    while (head) {
      if (head->next && seen.find(head->next) != seen.end()) {
        return head->next;
      }

      seen.insert(head);
      head = head->next;
    }

    return nullptr;
  }
};
