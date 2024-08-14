#include <iostream>
#include <vector>
class Solution {
public:
    int search(std::vector<int>& nums, int target)
    {
        int length = nums.size();
        int left = 0;
        int right = length - 1;
        while (left <= right) {
            int middle = left + (right - left) / 2;
            if (target == nums[middle]) {
                return middle;
            } else if (target < nums[middle]) {
                right = middle - 1;
            } else {
                left = middle + 1;
            }
        }
        return -1;
    }
};

int main()
{
    Solution s;
    std::vector<int> nums = { 1, 2, 3, 4 };
    int res = s.search(nums, 4);
    std::cout << res << std::endl;
}
