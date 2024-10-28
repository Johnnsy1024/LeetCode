from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        global_max_val = nums[0]
        cur_min_val = nums[0]
        cur_max_val = nums[0]
        for i in range(1, len(nums)):
            tmp1 = min(nums[i], nums[i] * cur_min_val, nums[i] * cur_max_val)
            tmp2 = max(nums[i], nums[i] * cur_min_val, nums[i] * cur_max_val)
            global_max_val = max(global_max_val, tmp1, tmp2)
            cur_min_val = tmp1
            cur_max_val = tmp2
        return global_max_val


nums = [-2, 3, -4]
print(Solution().maxProduct(nums))
