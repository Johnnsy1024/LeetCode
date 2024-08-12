/*
 * @lc app=leetcode.cn id=209 lang=cpp
 *
 * [209] 长度最小的子数组
 */
#include <climits>
#include <iostream>
#include <vector>
using namespace std;

// @lc code=start
class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums)
    {
        int res = INT_MAX;
        int sum = 0;
        int start = 0;
        for (int fast = 0; fast < nums.size(); fast++) {
            sum += nums[fast];
            while (sum >= target) {
                if (res > fast - start + 1) {
                    res = fast - start + 1;
                }
                sum -= nums[start];
                start++;
            }
        }
        return res < INT_MAX ? res : 0;
    }
};
// @lc code=end
int main()
{
    Solution s;
    int target = 15;
    vector<int> nums = { 5, 1, 3, 5, 10, 7, 4, 9, 2, 8 };
    int res = s.minSubArrayLen(target, nums);
    cout << res << endl;
}