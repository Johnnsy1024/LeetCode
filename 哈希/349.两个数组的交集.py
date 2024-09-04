from typing import List


class Solution:
    # set做法
    # def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    #     s1 = set(nums1)
    #     s2 = set(nums2)
    #     return list(s1 & s2)
    # 数组哈希做法
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr1 = [0] * 1001
        arr2 = [0] * 1001
        res = []
        for i in nums1:
            arr1[i] += 1
        for i in nums2:
            arr2[i] += 1
        for k in range(1001):
            if arr1[k] * arr2[k] > 0:
                res.append(k)
        return res


if __name__ == "__main__":
    print(Solution().intersection([1, 2, 2, 1], [2, 2]))
