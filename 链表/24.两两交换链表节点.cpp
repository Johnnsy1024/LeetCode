#include <cstddef>
#include <iostream>

struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr)
    {
    }
    ListNode(int x) : val(x), next(nullptr)
    {
    }
    ListNode(int x, ListNode *next) : val(x), next(next)
    {
    }
};
class Solution
{
  public:
    ListNode *swapPairs(ListNode *head)
    {
        if (head->next == NULL || head == NULL)
        {
            return head;
        }
        ListNode *prev = head;
        ListNode *cur = head->next;
        ListNode *next = head->next->next;

        cur->next = prev;
        prev->next = swapPairs(next);
        return cur;
    }
};

int main()
{
}