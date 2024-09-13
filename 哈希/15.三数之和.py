from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """重点在于三个位置对应数值的去重trick

        Args:
            nums (List[int]): _description_

        Returns:
            List[List[int]]: _description_
        """
        nums = sorted(nums)
        res = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # 为什么？因为重复的i对应的nums值的全部可能已经在右侧搜索过了
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return res


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    print(Solution().threeSum(nums))
