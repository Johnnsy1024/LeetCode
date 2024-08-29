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

    ListNode *swapPair2(ListNode *head)
    {
        ListNode *dummy = new ListNode(0);
        dummy->next = head;
        ListNode *temp = dummy;
        while (temp->next != nullptr && temp->next->next != nullptr)
        {
            ListNode *node1 = temp->next;
            ListNode *node2 = temp->next->next;
            temp->next = node2;
            node1->next = node2->next;
            node2->next = node1;
            temp = node1;
        }
        ListNode *res = dummy->next;
        delete dummy;
        return res;
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