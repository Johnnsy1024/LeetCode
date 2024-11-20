from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        def heapify(nums: List[int], root: int, n: int):
            largest = root
            left = 2 * largest + 1
            right = 2 * largest + 2
            if left < n and nums[left] > nums[largest]:
                largest = left
            if right < n and nums[right] > nums[largest]:
                largest = right
            if largest != root:
                nums[largest], nums[root] = nums[root], nums[largest]
                heapify(nums, largest, n)

        n = len(nums)
        for i in range(n // 2 - 1, -1, -1):
            heapify(nums, i, n)
        # 此时nums[0]为最大值
        for i in range(n - 1, n - k, -1):
            nums[0], nums[i] = nums[i], nums[0]
            heapify(nums, 0, i)
        return nums[0]


if __name__ == "__main__":
    nums = [3, 2, 1, 5, 6, 4]
    print(Solution().findKthLargest(nums, 2))
