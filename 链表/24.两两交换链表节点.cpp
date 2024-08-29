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
        if (head == NULL || head->next == NULL)
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
    ListNode *head = new ListNode(1);
    head->next = new ListNode(2);
    head->next->next = new ListNode(3);
    head->next->next->next = new ListNode(4);
    Solution s;
    ListNode *res = s.swapPairs(head);

    while (res != nullptr)
    {
        std::cout << res->val << " ";
        res = res->next;
    }
    std::cout << std::endl;

    // 释放内存
    while (head != nullptr)
    {
        ListNode *temp = head;
        head = head->next;
        delete temp;
    }

    return 0;
}