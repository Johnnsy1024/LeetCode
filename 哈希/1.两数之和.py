from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        records = dict()

        for index, value in enumerate(nums):
            if target - value in records:  # 遍历当前元素，并在map中寻找是否有匹配的key
                return [records[target - value], index]
            records[value] = index  # 如果没找到匹配对，就把访问过的元素和下标加入到map中
        return []


if __name__ == "__main__":
    nums = [3, 2, 4]
    target = 6
    print(Solution().twoSum(nums, target))
