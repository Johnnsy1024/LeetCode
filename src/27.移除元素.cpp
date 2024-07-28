/*
 * @lc app=leetcode.cn id=27 lang=cpp
 *
 * [27] 移除元素
 */
extern int apppp;
// @lc code=start
#include <iostream>
#include <vector>
class Solution {
public:
    int removeElement(std::vector<int>& nums, int val)
    {
        int slow = 0;
        int fast = 0;
        while (fast < nums.size()) {
            if (nums[fast] != val) {
                nums[slow] = nums[fast];
                slow++;
                fast++;
            } else {
                fast++;
            }
        }
        return slow;
    }
};
// @lc code=end

int main()
{
    Solution s;
    std::vector<int> nums = { 0, 1, 2, 2, 3, 0, 4, 2 };
    int res = s.removeElement(nums, 2);
    std::cout << res << std::endl;
}