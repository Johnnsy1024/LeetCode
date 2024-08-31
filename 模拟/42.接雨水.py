from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """接雨水的核心思想:
        当前位置i能接的雨水数量等于当前位置左边的最大值与右边最大值之间的最小值(木桶效应)减去位置i的高度

        Args:
            height (List[int]): _description_

        Returns:
            int: _description_
        """
        n = len(height)
        pre_max, suf_max = [0 for _ in range(n)], [0 for _ in range(n)]
        pre_max[0] = height[0]
        suf_max[n - 1] = height[n - 1]
        for i in range(1, n):
            pre_max[i] = max(pre_max[i - 1], height[i])
        for i in range(n - 2, -1, -1):
            suf_max[i] = max(suf_max[i + 1], height[i])

        res = 0
        for i in range(n):
            tmp = min(pre_max[i], suf_max[i])
            res += tmp - height[i]
        return res


if __name__ == "__main__":
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(Solution().trap(height))
