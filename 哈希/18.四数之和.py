from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """n数之和的题目,都不适合用哈希法,而应该统一用三数,四数之和模版的双指针法

        Args:
            nums (List[int]): _description_
            target (int): _description_

        Returns:
            List[List[int]]: _description_
        """
        nums = sorted(nums)
        n = len(nums)
        res = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                left = j + 1
                right = n - 1
                while left < right:
                    tmp = nums[i] + nums[j] + nums[left] + nums[right]
                    if tmp == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    if tmp > target:
                        right -= 1
                    if tmp < target:
                        left += 1
        return res


if __name__ == "__main__":
    print(Solution().fourSum([1, 0, -1, 0, -2, 2], 0))
