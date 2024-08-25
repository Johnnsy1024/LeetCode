from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        l, r, t, b = 0, n - 1, 0, n - 1
        cur_num = 1
        res = [[0 for _ in range(n)] for _ in range(n)]
        while True:
            for i in range(l, r + 1):
                res[t][i] = cur_num
                cur_num += 1
            t += 1
            if t > b:
                break
            for i in range(t, b + 1):
                res[i][r] = cur_num
                cur_num += 1
            r -= 1
            if l > r:
                break
            for i in range(r, l - 1, -1):
                res[b][i] = cur_num
                cur_num += 1
            b -= 1
            if b < t:
                break
            for i in range(b, t - 1, -1):
                res[i][l] = cur_num
                cur_num += 1
            l += 1
            if l > r:
                break
        return res


if __name__ == "__main__":
    n = 6
    print(Solution().generateMatrix(n))
