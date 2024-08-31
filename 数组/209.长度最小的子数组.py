from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """关键在于双指针对应的滑动窗口

        Args:
            target (int): _description_
            nums (List[int]): _description_

        Returns:
            int: _description_
        """
        slow = 0
        fast = 0
        cur = 0
        res = float("inf")
        while fast < len(nums):
            cur += nums[fast]
            while cur >= target:
                res = min(res, fast - slow + 1)
                cur -= nums[slow]
                slow += 1
            fast += 1
        return res if res != float("inf") else 0


if __name__ == "__main__":
    nums = [2, 3, 1, 2, 4, 3]
    print(Solution().minSubArrayLen(7, nums))
