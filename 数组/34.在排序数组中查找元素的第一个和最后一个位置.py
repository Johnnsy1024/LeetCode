from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left_border = self.get_left_border(nums, target)
        right_border = self.get_right_border(nums, target)
        if left_border == -1 and right_border == -1:
            return [-1, -1]
        else:
            return [left_border, right_border]

    def get_left_border(self, nums: List[int], target: int):
        """获得target的左边界
        关键在于设定一个初始的边界下标值,如果找到了新的下标,则更新,否则返回这个设定的初始下标值(-1)

        Args:
            nums (List[int]): 子数组
            target (int): 目标值

        Returns:
            _type_: _description_
        """
        left = 0
        right = len(nums) - 1
        left_border = -1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] == target:
                left_border = mid
                right = mid - 1
        return left_border

    def get_right_border(self, nums: List[int], target: int):
        """获得target的右边界

        Args:
            nums (List[int]): 子数组
            target (int): 目标值
        """
        left = 0
        right = len(nums) - 1
        right_border = -1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            if nums[mid] > target:
                right = mid - 1
            if nums[mid] == target:
                right_border = mid
                left = mid + 1
        return right_border


if __name__ == "__main__":
    nums = []
    print(Solution().searchRange(nums, 0))
