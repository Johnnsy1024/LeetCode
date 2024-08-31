from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """以数组第i个元素为末尾的最大子数组和为当前元素和当前元素与以第i-1个元素为末尾的最大子数组和只和的较大值

        Args:
            nums (List[int]): _description_

        Returns:
            int: _description_
        """
        max_val = -float("inf")
        prev = -float("inf")
        for i in range(len(nums)):
            tmp = max(nums[i], nums[i] + prev)
            if tmp > max_val:
                max_val = tmp
            prev = tmp
        return max_val


if __name__ == "__main__":
    print(Solution().maxSubArray([5, 4, -1, 7, 8]))
