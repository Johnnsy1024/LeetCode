/*
 * @lc app=leetcode.cn id=34 lang=cpp
 *
 * [34] 在排序数组中查找元素的第一个和最后一个位置
 */

// @lc code=start
#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target)
    {
        int leftBorder = getLeftBorder(nums, target);
        int rightBorder = getRightBorder(nums, target);
        // 情况一
        if (leftBorder == -2 || rightBorder == -2)
            return { -1, -1 };
        // 情况三
        if (rightBorder - leftBorder >= 0)
            return { leftBorder, rightBorder };
        // 情况二
        return { -1, -1 };
    }

private:
    int getRightBorder(vector<int>& nums, int target)
    {
        int left = 0;
        int right = nums.size() - 1;
        int rightBorder = -2; // 记录一下rightBorder没有被赋值的情况
        while (left <= right) {
            int middle = left + ((right - left) / 2);
            if (nums[middle] > target) {
                right = middle - 1;
            } else if (nums[middle] < target) {
                left = middle + 1;
            } else { //当middle对应着target的时候，由于是寻找右边界，所以给left+1，然后将left赋值给rightBorder
                left = middle + 1;
                rightBorder = left - 1;
            }
        }
        return rightBorder;
    }
    int getLeftBorder(vector<int>& nums, int target)
    {
        int left = 0;
        int right = nums.size() - 1;
        int leftBorder = -2; // 记录一下leftBorder没有被赋值的情况
        while (left <= right) {
            int middle = left + ((right - left) / 2);
            if (nums[middle] == target) { // 寻找左边界，nums[middle] == target的时候更新right
                right = middle - 1;
                leftBorder = right + 1;
            } else if (nums[middle] < target) {
                left = middle + 1;
            } else {
                right = middle - 1;
            }
        }
        return leftBorder;
    }
};
// @lc code=end

int main()
{
    vector<int> nums = { 1 };
    Solution s;
    vector<int> res = s.searchRange(nums, 1);
    for (int i = 0; i < res.size(); i++) {
        cout << res[i] << " ";
    }
    cout << endl;
}