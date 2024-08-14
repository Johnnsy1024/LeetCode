#include <iostream>
#include <vector>
class Solution {
public:
    int searchInsert(std::vector<int>& nums, int target)
    {
        int left = 0;
        int right = nums.size() - 1;
        while (left <= right) {
            int middle = left + (right - left) / 2;
            if (target == nums[middle]) {
                return middle;
            } else if (target > nums[middle]) {
                left = middle + 1;
            } else {
                right = middle - 1;
            }
        }
        return left;
    }
};

int main()
{
    Solution s;
    std::vector<int> nums = { 1, 3, 5, 6 };
    int target = 3;
    int res = s.searchInsert(nums, target);
    std::cout << res << std::endl;
}
