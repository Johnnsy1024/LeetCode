from typing import List


class Solution:
    def fourSumCount(
        self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]
    ) -> int:
        hashmap = {}
        cnt = 0
        for i in nums1:
            for j in nums2:
                if i + j in hashmap:
                    hashmap[i + j] += 1
                else:
                    hashmap[i + j] = 1
        for i in nums3:
            for j in nums4:
                if -i - j in hashmap:
                    cnt += hashmap[-i - j]
        return cnt


if __name__ == "__main__":
    print(Solution().fourSumCount([1, 2], [-2, -1], [-1, 2], [0, 2]))
